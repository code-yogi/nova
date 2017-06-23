/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// URLS:api-
//var url_empleados_bypage = window.location.origin + "/api-ebs/viewempleadosfull_bypage/"

// OBJS
var tarjeta_resultados = null
var popup_acciones = null
var popup_nuevo = null
var popup_editarA = null
var popup_evaluacion = null
var toolbar = null
var grid = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {
    
    tarjeta_resultados = new TarjetaResultados()
})

/*-----------------------------------------------*\
            OBJETO: Tarjeta resultados
\*-----------------------------------------------*/

function TarjetaResultados() {

    toolbar = new ToolBar()
    grid = new Grid()
}

/*-----------------------------------------------*\
            OBJETO: toolbar
\*-----------------------------------------------*/

function ToolBar() {

    popup_nuevo = new PopupNuevo()
}

/*-----------------------------------------------*\
            OBJETO: grid
\*-----------------------------------------------*/

function Grid() {

    popup_acciones = new PopupAcciones()
    popup_editarA = new PopupEditarA()
    popup_evaluacion = new PopupEvaluacion()
}

/*-----------------------------------------------*\
            OBJETO: popup acciones
\*-----------------------------------------------*/

function PopupAcciones () {
 
    this.$id_tarjeta_acciones = $('#id_tarjeta_acciones')
    this.$id_boton_evaluacion_eficacia = $('#id_boton_evaluacion_eficacia')
    this.$id_boton_editar_accion = $('#id_boton_editar_accion')
    this.init_Events()
}
PopupAcciones.prototype.init_Events = function () {

    this.$id_boton_editar_accion.on("click", this, this.click_Boton_Editar )
    this.$id_boton_evaluacion_eficacia.on("click", this, this.click_BotonEvaluacion)
}
PopupAcciones.prototype.click_Boton_Editar = function (e) {

    e.preventDefault()
    e.data.$id_tarjeta_acciones.modal('hide')
}
PopupAcciones.prototype.click_BotonEvaluacion = function (e) {

    e.preventDefault()
    e.data.$id_tarjeta_acciones.modal('hide')
}
function PopupNuevo () {

    this.$id_actividad = $('#id_actividad')
    this.$id_responsable = $('#id_responsable')
    this.$id_fecha_programada = $('#id_fecha_programada')
    this.$id_fecha_programada_input = $('#id_fecha_programada_input')
    this.init_Components()
}
PopupNuevo.prototype.init_Components = function () {

    this.$id_actividad.wysihtml5(appnova.get_ConfWysi())
    this.$id_responsable.select2(appnova.get_ConfigSelect2())
    this.$id_fecha_programada.mask(
        "9999-99-99",
        {
            placeholder:"aaaa/mm/dd"
        }
    )
    this.$id_fecha_programada_input.datetimepicker(this.get_DateTimePickerConfig())
}
PopupNuevo.prototype.get_DateTimePickerConfig = function () {
    return {
        autoclose: true,
        orientation: "bottom left",
        minViewMode: 2,
        format: "yyyy-mm-dd",
    }
}

/*-----------------------------------------------*\
            OBJETO: popup editarA
\*-----------------------------------------------*/

function PopupEditarA () {

    this.$id_evidencia = $('#id_evidencia')
    this.$id_plan_observaciones = $('#id_plan_observaciones')
    this.init_Components()
}
PopupEditarA.prototype.init_Components = function () {

    this.$id_evidencia.wysihtml5(appnova.get_ConfWysi())
    this.$id_plan_observaciones.wysihtml5(appnova.get_ConfWysi())
}

/*-----------------------------------------------*\
            OBJETO: popup evaluacion
\*-----------------------------------------------*/

function PopupEvaluacion () {

    this.$id_plan_resultado = $('#id_plan_resultado')
    this.$id_causas = $('#id_causas')
    this.$id_fecha_seguimiento = $('#id_fecha_seguimiento')
    this.$id_fecha_seguimiento_input = $('#id_fecha_seguimiento_input')
    this.$id_imagen = $('#id_imagen')
    this.init_Components()
}
PopupEvaluacion.prototype.init_Components = function () {

    this.$id_plan_resultado.select2(appnova.get_ConfigSelect2())
    this.$id_causas.wysihtml5(appnova.get_ConfWysi())
    this.$id_fecha_seguimiento.mask(
        "9999-99-99",
        {
            placeholder:"aaaa/mm/dd"
        }
    )
    this.$id_fecha_seguimiento_input.datetimepicker(this.get_DateTimePickerConfig())
    this.$id_imagen.each(function(){
        var $input   = $( this ),
            $label   = $input.next( 'label' ),
            labelVal = $label.html();

        $input.on( 'change', function( e )
        {
            var fileName = '';

            if( this.files && this.files.length > 1 )
              fileName = ( this.getAttribute( 'data-multiple-caption' ) || '' ).replace( '{count}', this.files.length );
            else if( e.target.value )
              fileName = e.target.value.split( '\\' ).pop();

            if( fileName )
              $label.find( 'span' ).html( fileName );
            else
              $label.html( labelVal );
        });
        }
    )
}
PopupEvaluacion.prototype.get_DateTimePickerConfig = function () {
    return {
        autoclose: true,
        orientation: "bottom left",
        minViewMode: 2,
        format: "yyyy-mm-dd",
    }
}