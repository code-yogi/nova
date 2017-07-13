/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/
var url_documento_personal = window.location.origin  + "/api-capitalhumano/documentopersonal/"
var url_documento_capacitacion = window.location.origin  + "/api-capitalhumano/documentocapacitacion/"
var url_archivo =  window.location.origin + "/api-capitalhumano/archivo/"
var url_expediente_personal_bypage = window.location.origin  + "/api-capitalhumano/documentopersonal_bypage/"
var url_expediente_capacitacion_bypage = window.location.origin  + "/api-capitalhumano/documentocapacitacion_bypage/"
var url_eliminar = window.location.origin + "/expedientes/"
var url_profile =  window.location.origin + "/api-seguridad/profile/"


// OBJS
var popup = null
var popup_cap = null
var toolbar = null
var grid_personal = null
var grid_capacitacion = null
var filtro = null
var tarjeta_resultados = null
var personalizacion = null

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {
    filtro = new Filtro()
    tarjeta_resultados = new TarjetaResultados()

})

/*-----------------------------------------------*\
            OBJETO: Tarjeta Resultados
\*-----------------------------------------------*/

function TarjetaResultados(){
    popup = new PopupPersonal()
    popup_cap = new PopupCapacitacion()
    toolbar = new Toolbar()
    personalizacion = new Personalizacion
    grid_personal = new GridPersonal()
}

/*-----------------------------------------------*\
            OBJETO: Componentes
\*-----------------------------------------------*/

function Filtro(){

    this.$numero_empleado = $('#numero_empleado')
}
Filtro.prototype.get_Values = function (_page) {
    return {
        page: _page,
        relacion_personal__numero_empleado: this.$numero_empleado.val(),
   }
}
Filtro.prototype.get_ValuesCap = function (_page) {
    return {
        page: _page,
        relacion_capacitacion__numero_empleado: this.$numero_empleado.val(),
   }
}


/*-----------------------------------------------*\
            OBJETO: Pop up personal
\*-----------------------------------------------*/

function PopupPersonal () {

    this.$modal_per = $('#modal_nuevo')
    this.$formulario_per = $('#formulario_per')
    this.$boton_nuevo = $('#boton_nuevo_per')
    this.$boton_guardar = $('#id_boton_guardar_personal')

    this.$numero_empleado = $('#numero_empleado')
    this.$tipo_documento = $('#id_tipo_documento')
    this.$agrupador = $('#id_agrupador')
    this.$vigencia_inicio = $('#id_vigencia_inicio')
    this.$vigencia_fin = $('#id_vigencia_fin')
    this.$vigencia_inicio_input = $('#id_vigencia_inicio_input')
    this.$vigencia_fin_input = $('#id_vigencia_fin_input')
    this.$created_by = $('#created_by')
    this.$archivo = $('#id_archivo')

    this.init_Components()
    this.init_Events()
}
PopupPersonal.prototype.init_Components = function () {

    this.$tipo_documento.select2(appnova.get_ConfigSelect2())
    this.$agrupador.select2(appnova.get_ConfigSelect2())
    this.$vigencia_inicio.mask("9999-99-99",{  placeholder:"aaaa/mm/dd"  })
    this.$vigencia_inicio_input.datetimepicker(this.get_DateTimePickerConfig())
    this.$vigencia_fin.mask("9999-99-99",{  placeholder:"aaaa/mm/dd"  })
    this.$vigencia_fin_input.datetimepicker(this.get_DateTimePickerConfig())
}
PopupPersonal.prototype.init_Events = function () {

   this.$boton_guardar.on('click', this, this.click_BotonGuardar)
}
PopupPersonal.prototype.get_DateTimePickerConfig = function () {
    return {
        autoclose: true,
        orientation: "bottom left",
        minViewMode: 2,
        format: "yyyy-mm-dd",
    }
}
PopupPersonal.prototype.click_BotonGuardar = function (e) {

    var promesa = $.ajax({
         url: url_documento_personal,
         method: "POST",
         headers: { "X-CSRFToken": appnova.galletita },
         data: {
            'numero_empleado' : e.data.$numero_empleado.val(),
            'tipo_documento' : e.data.$tipo_documento.val(),
            'agrupador' : e.data.$agrupador.val(),
            'vigencia_inicio' : e.data.$vigencia_inicio.val(),
            'vigencia_fin' : e.data.$vigencia_fin.val(),
            'created_by' : url_profile+e.data.$created_by.val()+"/",
         },
         success: function (_response) {
         },
         error: function (_response) {
            alertify.error("Ocurrio error al guardar")
         }
      })
    promesa.then(function(){
        popup.buscar_UltimoRegistro()
    })
}
PopupPersonal.prototype.buscar_UltimoRegistro = function () {

    $.ajax({
         url: url_documento_personal,
         method: "GET",
         success: function (_response) {
            posicion = _response.length - 1
            id_personal = _response[posicion].pk
            popup.guardar_Archivo(id_personal)
         },
         error: function (_response) {
            alertify.error("Ocurrio error al consultar")
         }
    })
}
PopupPersonal.prototype.guardar_Archivo = function (_id_personal){

    var data = new FormData()
     popup.$formulario_per.find(':input').each(function() {
        var elemento= this;
        if(elemento.type === 'file'){
           if(elemento.value !== ''){
                for(var i=0; i< $('#'+elemento.id).prop("files").length; i++){
                  data.append('archivo', $('#'+elemento.id).prop("files")[i]);
               }
              
                data.append('tipo_archivo', "per")
                data.append('content_object', url_documento_personal+_id_personal+"/")
                data.append('created_by', url_profile+popup.$created_by.val()+"/")
            }              
         }
     })

     $.ajax({
         url: url_archivo,
         method: "POST",
         headers: { "X-CSRFToken": appnova.galletita },
         contentType: false,
         processData: false,
         data: data,
         success: function (_response) {

            alert('Se ha guardado el archivo')
            popup.hidden_Modal()
            popup.actualizar_Grid()
         },
         error: function (_response) {

            alertify.error("Ocurrio error al guardar archivo")
         }
      })
}
PopupPersonal.prototype.hidden_Modal = function () {

   this.$modal_per.modal('hide')
   this.limpiar_Formulario()
}
PopupPersonal.prototype.actualizar_Grid = function () {
    $("#grid_resultados").empty()
    grid_personal.init()
}
PopupPersonal.prototype.limpiar_Formulario = function () {

    this.$tipo_documento.data('select2').val(0)
    this.$agrupador.data('select2').val(0)
    this.$vigencia_inicio.val("")
    this.$vigencia_fin.val("")
    this.$archivo.val("")

}

/*-----------------------------------------------*\
            OBJETO: POPUP CAPACITACION
\*-----------------------------------------------*/

function PopupCapacitacion () {

    this.$modal_cap = $('#modal_nuevo_cap')
    this.$formulario_cap = $('#form_capacitacion')
    this.$boton_nuevo = $('#boton_nuevo_cap')
    this.$boton_guardar = $('#id_boton_guardar_capacitacion')

    this.$numero_empleado = $('#numero_empleado')
    this.$proveedor = $('#id_proveedor')
    this.$lugar = $('#id_lugar')
    this.$costo = $('#id_costo')
    this.$duracion = $('#id_duracion')
    this.$observaciones = $('#id_observaciones')
    this.$agrupadorcap = $('#id_agrupadorcap')
    this.$area = $('#id_area')
    this.$curso = $('#id_curso')
    this.$modalidad = $('#id_modalidad')
    this.$moneda = $('#id_moneda')
    this.$departamento = $('#id_departamento')
    this.$fecha_inicio = $('#id_fecha_inicio')
    this.$fecha_inicio_input = $('#id_fecha_inicio_input')
    this.$fecha_fin = $('#id_fecha_fin')
    this.$fecha_fin_input = $('#id_fecha_fin_input')
    this.$created_by = $('#created_by')
    this.$archivo_cap = $('#archivocap')

    this.init_Components()
    this.init_Events()
}
PopupCapacitacion.prototype.init_Components = function () {

    this.$agrupadorcap.select2(appnova.get_ConfigSelect2())
    this.$area.select2(appnova.get_ConfigSelect2())
    this.$curso.select2(appnova.get_ConfigSelect2())
    this.$modalidad.select2(appnova.get_ConfigSelect2())
    this.$moneda.select2(appnova.get_ConfigSelect2())
    this.$departamento.select2(appnova.get_ConfigSelect2())
    this.$fecha_inicio.mask("9999-99-99",{  placeholder:"aaaa/mm/dd"  })
    this.$fecha_inicio_input.datetimepicker(this.get_DateTimePickerConfig())
    this.$fecha_fin.mask("9999-99-99",{  placeholder:"aaaa/mm/dd"  })
    this.$fecha_fin_input.datetimepicker(this.get_DateTimePickerConfig())
}
PopupCapacitacion.prototype.init_Events = function () {

   this.$boton_guardar.on('click', this, this.click_BotonGuardar)
}
PopupCapacitacion.prototype.get_DateTimePickerConfig = function () {
    return {
        autoclose: true,
        orientation: "bottom left",
        minViewMode: 2,
        format: "yyyy-mm-dd",
    }
}
PopupCapacitacion.prototype.click_BotonGuardar = function (e) {
    var promesa = $.ajax({
         url: url_documento_capacitacion,
         method: "POST",
         headers: { "X-CSRFToken": appnova.galletita },
         data: {
            'numero_empleado' : e.data.$numero_empleado.val(),
            'curso' : e.data.$curso.val(),
            'proveedor' : e.data.$proveedor.val(),
            'modalidad' : e.data.$modalidad.val(),
            'lugar' : e.data.$lugar.val(),
            'costo' : e.data.$costo.val(),
            'moneda' : e.data.$moneda.val(),
            'departamento' : e.data.$departamento.val(),
            'fecha_inicio' : e.data.$fecha_inicio.val(),
            'fecha_fin' : e.data.$fecha_fin.val(),
            'duracion' : e.data.$duracion.val(),
            'observaciones' : e.data.$observaciones.val(),
            'agrupador' : e.data.$agrupadorcap.val(),
            'area' : e.data.$area.val(),
            'created_by' : url_profile+e.data.$created_by.val()+"/",
         },
         success: function (_response) {
         },
         error: function (_response) {
            alertify.error("Ocurrio error al guardar")
         }
      })
    promesa.then(function(){
        popup_cap.buscar_UltimoRegistro()
    })
}
PopupCapacitacion.prototype.buscar_UltimoRegistro = function () {

    $.ajax({
         url: url_documento_capacitacion,
         method: "GET",
         success: function (_response) {
            posicion = _response.length - 1
            id_personal = _response[posicion].pk
            popup_cap.guardar_Archivo(id_personal)
         },
         error: function (_response) {
            alertify.error("Ocurrio error al consultar")
         }
    })
}
PopupCapacitacion.prototype.guardar_Archivo = function (_id_personal){
    // e.stopPropagation()
    // e.preventDefault()
    var data = new FormData()
     popup_cap.$formulario_cap.find(':input').each(function() {
        var elemento= this;
        if(elemento.type === 'file'){
           if(elemento.value !== ''){
                for(var i=0; i< $('#'+elemento.id).prop("files").length; i++){
                  data.append('archivo', $('#'+elemento.id).prop("files")[i]);
               }
              
                data.append('tipo_archivo', "cap")
                data.append('content_object', url_documento_capacitacion+_id_personal+"/")
                data.append('created_by', url_profile+popup_cap.$created_by.val()+"/")
            }              
         }
     })

     $.ajax({
         url: url_archivo,
         method: "POST",
         headers: { "X-CSRFToken": appnova.galletita },
         contentType: false,
         processData: false,
         data: data,
         success: function (_response) {

            alert('Se ha guardado el archivo')
            popup_cap.hidden_Modal()
            popup_cap.actualizar_Grid()
         },
         error: function (_response) {

            alertify.error("Ocurrio error al guardar archivo")
         }
      })
}
PopupCapacitacion.prototype.hidden_Modal = function () {

   this.$modal_cap.modal('hide')
   this.limpiar_Formulario()
}
PopupCapacitacion.prototype.actualizar_Grid = function () {
    $("#grid_resultados").empty()
    grid_capacitacion.init()
}
PopupCapacitacion.prototype.limpiar_Formulario = function () {

    this.$proveedor.val("")
    this.$lugar.val("")
    this.$costo.val("")
    this.$duracion.val("")
    this.$observaciones.val("")
    this.$agrupadorcap.data('select2').val(0)
    this.$area.data('select2').val(0)
    this.$curso.data('select2').val(0)
    this.$modalidad.data('select2').val(0)
    this.$moneda.data('select2').val(0)
    this.$departamento.data('select2').val(0)
    this.$fecha_inicio.val("")
    this.$fecha_fin.val("")
    this.$archivo_cap.val("")
}

/*-----------------------------------------------*\
            OBJETO: TOOLBAR
\*-----------------------------------------------*/

function Toolbar() {
    
    this.$boton_nuevo = $('#boton_nuevo')
    this.init_Events()
}
Toolbar.prototype.init_Events = function () {

    this.$boton_nuevo.on("click", this, this.mostrar_Modal)
    // this.$boton_nuevo_cap.on("click", this, this.mostrar_Modal) 
}
Toolbar.prototype.mostrar_Modal = function (e){
    
    // popup_per.$id.hasClass('in')
}
Toolbar.prototype.mostrar_ModalCap = function (e){
    
    popup_cap.$id.hasClass('in')
}

/*-----------------------------------------------*\
            OBJETO: FILTRO ARCHIVOS
\*-----------------------------------------------*/

function Personalizacion(){
    this.$personales = $('#personales')
    this.$capacitaciones = $('#capacitaciones')
    this.init_Events()
}
Personalizacion.prototype.init_Components = function(){
}
Personalizacion.prototype.init_Events = function(){
    
    this.$personales.on("click", this , this.mostrar_Personales)
    this.$capacitaciones.on("click", this , this.mostrar_Capacitaciones)
}
Personalizacion.prototype.mostrar_Personales = function(e){
    
    e.data.$capacitaciones.removeClass('nova-active-tab')
    e.data.$personales.addClass('nova-active-tab')
    popup_cap.$boton_nuevo.addClass('hidden')
    popup.$boton_nuevo.removeClass('hidden')
    $("#grid_resultados").empty()
    grid_personal.init()
}
Personalizacion.prototype.mostrar_Capacitaciones = function(e){
    
    e.data.$personales.removeClass('nova-active-tab')
    e.data.$capacitaciones.addClass('nova-active-tab')
    popup.$boton_nuevo.addClass('hidden')
    popup_cap.$boton_nuevo.removeClass('hidden')
    $("#grid_resultados").empty()
    grid_capacitacion = new GridCapacitacion()
}

/*-----------------------------------------------*\
            OBJETO: Grid personal
\*-----------------------------------------------*/

function GridPersonal() {

    this.$id = $("#grid_resultados")
    this.kfuente_datos = null

    this.kgrid = null
    this.init()
}
GridPersonal.prototype.init = function () {

    // Definicion del pais, formato modena, etc..
    kendo.culture("es-MX")

    // Se inicializa la fuente da datos (datasource)
    this.kfuente_datos = new kendo.data.DataSource(this.get_DataSourceConfig())
    
    // Se inicializa y configura el grid:
    this.kgrid = this.$id.kendoGrid(this.get_Configuracion())
}
GridPersonal.prototype.get_DataSourceConfig = function () {
    return {

        serverPaging: true,
        pageSize: 10,
        transport: {
            read: {
                url: url_expediente_personal_bypage,
                type: "GET",
                dataType: "json",
            },
            parameterMap: function (data, action) {
                if (action === "read"){
                    return  filtro.get_Values(data.page)
                }
            }
        },
        schema: {
            data: "results",
            total: "count",
            model: {
                fields: this.get_Campos()
            }
        },
        error: function (e) {
            alertify.error("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    }    
}
GridPersonal.prototype.get_Campos = function () {
    
    return {
        pk: {type: "string"},
        agrupador : { type: "string" },
        fecha : { type: "date"},
        vigencia_inicio : { type: "string" },
        vigencia_fin : { type: "string" },
        tipo_documento : { type: "string" },
        archivo : { type: "string" },
        created_by : { type: "string" },
        created_date : { type: "date" },
        object_id: { type: "integer" },
        numero_empleado: { type: "string" },
    }
}
GridPersonal.prototype.get_Configuracion = function () {

    return {
        dataSource: this.kfuente_datos,
        columnMenu: true,
        groupable: false,
        sortable: false,
        editable: false,
        resizable: true,
        selectable: true,
        columns: this.get_Columnas(),
        scrollable: true,
        pageable: true,
        noRecords: {
            template: "<div class='grid-empty'> No se encontraron registros </div>"
        },
        dataBound: this.set_Icons,
    }
}
GridPersonal.prototype.get_Columnas = function () {

    return [  
        { field: "pk", 
          title: " ", 
          width:"50px" ,
          template: '<a href="#=url_eliminar + numero_empleado+ "/" + pk #/expediente/eliminar/personal/" class="btn nova-btn btn-default nova-btn-delete" id="boton_nuevo"> <i class="icon icon-left icon mdi mdi-delete nova-white"></i></a>',
        },
        { field: "tipo_documento", 
          title: "Archivo", 
          width:"150px" ,
          template: '<a href="#=archivo#" target="_blank">#=tipo_documento#</a>',
        },
        { field: "agrupador", title: "Agrupador", width:"100px"},
        { field: "vigencia_inicio",title: "Vigencia inicio",width:"100px"},
        { field: "vigencia_fin", title: "Vigencia fin", width:"100px" },
        { field: "created_by", title: "Creado por", width:"150px" },
        { field: "created_date", title: "Fecha de creación", width:"150px", format: "{0:dd/MM/yyyy}" },

    ]
}
GridPersonal.prototype.buscar = function() {

    this.kfuente_datos.page(1)
}

/*-----------------------------------------------*\
            OBJETO: Grid capacitacion
\*-----------------------------------------------*/

function GridCapacitacion() {

    this.$id = $("#grid_resultados")
    this.kfuente_datos = null

    this.kgrid = null
    this.init()
}
GridCapacitacion.prototype.init = function () {

    // Definicion del pais, formato modena, etc..
    kendo.culture("es-MX")

    // Se inicializa la fuente da datos (datasource)
    this.kfuente_datos = new kendo.data.DataSource(this.get_DataSourceConfig())
    
    // Se inicializa y configura el grid:
    this.kgrid = this.$id.kendoGrid(this.get_Configuracion())
}
GridCapacitacion.prototype.get_DataSourceConfig = function () {
    return {

        serverPaging: true,
        pageSize: 10,
        transport: {
            read: {
                url: url_expediente_capacitacion_bypage,
                type: "GET",
                dataType: "json",
            },
            parameterMap: function (data, action) {
                if (action === "read"){
                    return  filtro.get_ValuesCap(data.page)
                }
            }
        },
        schema: {
            data: "results",
            total: "count",
            model: {
                fields: this.get_CamposCap()
            }
        },
        error: function (e) {
            alertify.error("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    }    
}
GridCapacitacion.prototype.get_CamposCap = function () {
    return {
        pk: { type: "integer" },
        curso : { type: "string" },
        agrupador: { type: "string" },
        area: { type: "string" },
        proveedor : { type: "string"},
        modalidad : { type: "string" },
        costo : { type: "string" },
        moneda : { type: "integer" },
        departamento : { type: "string" },
        fecha_inicio : { type: "string" },
        fecha_fin : { type: "string" },
        duracion : { type: "string" },
        observaciones : { type: "string" },
        created_by : { type: "string" },
        created_date : { type: "date" },
    }
}
GridCapacitacion.prototype.get_Configuracion = function () {

    return {
        dataSource: this.kfuente_datos,
        columnMenu: true,
        groupable: false,
        sortable: false,
        editable: false,
        resizable: true,
        selectable: true,
        columns: this.get_Columnas(),
        scrollable: true,
        pageable: true,
        noRecords: {
            template: "<div class='grid-empty'> No se encontraron registros </div>"
        },
        dataBound: this.set_Icons,
    }
}
GridCapacitacion.prototype.get_Columnas = function () {

    return [  
        { field: "pk", 
          title: " ", 
          width:"60px" ,
          template: '<a href="#=url_eliminar + numero_empleado+ "/" + pk #/expediente/eliminar/capacitacion/" class="btn nova-btn btn-default nova-btn-delete" id="boton_nuevo"> <i class="icon icon-left icon mdi mdi-delete nova-white"></i></a>',
        },
        { field: "curso", 
          title: "Curso", 
          width:"150px" ,
          template: '<a href="#=archivo#" target="_blank">#=curso#</a>',
        },
        { field: "agrupador", title: "Agrupador", width:"100px"},
        { field: "area", title: "Area", width:"100px"},
        { field: "proveedor", title: "Proveedor", width:"150px"},
        { field: "modalidad",title: "Modalidad",width:"100px"},
        { field: "costo", title: "Costo", width:"100px" },
        { field: "moneda",title: "Moneda",width:"100px"},
        { field: "departamento",title: "Departamento",width:"150px"},
        { field: "fecha_inicio", title: "Fecha inicio", width:"100px" },
        { field: "fecha_fin",title: "Fecha fin",width:"100px"},
        { field: "duracion", title: "Duración", width:"100px",template: '#=duracion# hrs' },
        { field: "observaciones", title: "Observaciones", width:"200px" },
        { field: "created_by", title: "Creado por", width:"150px" },
        { field: "created_date", title: "Fecha de creación", width:"150px", format: "{0:dd/MM/yyyy}" },

    ]
}
GridCapacitacion.prototype.buscar = function() {

    this.kfuente_datos.page(1)
}

