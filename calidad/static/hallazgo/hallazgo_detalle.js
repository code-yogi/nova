/*-----------------------------------------------*\
         GLOBAL VARIABLES
\*-----------------------------------------------*/

// URLS:api-
//var url_empleados_bypage = window.location.origin + "/api-ebs/viewempleadosfull_bypage/"

// OBJS
var menu = null

var tarjeta_detalle_hallazgo = null

var tarjeta_analisis_causa = null
// var toolbar_analisis_causa = null
// var grid_analisis_causa = null
var popup_analisis = null

var tarjeta_plan_accion = null
// var toolbar_plan_accion = null
// var grid_plan_accion = null
var popup_actividad = null
var popup_acciones = null
var popup_evaluacion_plan = null
var popup_seguimiento_plan = null
// var popup_editarA = null //popup_editarA

var tarjeta_evidencia = null
// var toolbar_evidencia = null
// var grid_evidencia = null
var popup_evidencia = null

/*-----------------------------------------------*\
         LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

   menu = new Menu()
   tarjeta_detalle_hallazgo = new TarjetaDetalleHallazgo()
   tarjeta_analisis_causa = new TarjetaAnalisisCausa()
   tarjeta_plan_accion = new TarjetaPlanAccion()
   tarjeta_evidencia = new TarjetaEvidencia()
})

/*-----------------------------------------------*\
         OBJETO: Menu
\*-----------------------------------------------*/

function Menu() {

   this.$elemento_lista = $('#id_lista>a[href*=\\#]')
   this.$ventana = $(window)
   this.$topPosition = $('.nova-slider-menu').offset().top - 60
   this.$menu_flotante = $('.nova-slider-menu')
   this.init_Events()
}
Menu.prototype.init_Events = function () {

   this.$elemento_lista.on("click", this, this.click_ElementoLista)
   this.$ventana.on("scroll", this, this.scroll_Ventana)
   this.$ventana.on("resize", this, this.resize_Ventana)
   this.$lista_acciones = $("#lista_acciones")
}
Menu.prototype.click_ElementoLista = function () {

   $(this).addClass('active').siblings().removeClass('active')

   if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {

      var $target = $(this.hash)

      $target = $target.length && $target || $('[name=' + this.hash.slice(1) +']')

      if ($target.length) {
         var targetOffset = $target.offset().top
         $('html,body').animate({scrollTop: targetOffset-60}, 1000)
         return false
      }
   }
}
Menu.prototype.scroll_Ventana = function (e) {

   var menu_flotante_ancho = $('.nova-slider').outerWidth()
   e.data.$lista_acciones.css("width", menu_flotante_ancho)

   if (window.matchMedia('(min-width: 992px)').matches) {
      if ((e.data.$ventana.scrollTop() > e.data.$topPosition) ) {
         e.data.$menu_flotante.addClass('sticky')
      }
      else {
         e.data.$menu_flotante.removeClass('sticky')
      }
   }
   else {
      e.data.$menu_flotante.removeClass('sticky')
   }
}
Menu.prototype.resize_Ventana = function (e) {

   var menu_flotante_ancho = $('.nova-slider').outerWidth()
   e.data.$lista_acciones.css("width", menu_flotante_ancho)

   if (window.matchMedia('(max-width: 992px)').matches) {
      e.data.$menu_flotante.addClass('nova-slider-menu-fixed')
   }
   else {
      e.data.$menu_flotante.removeClass('nova-slider-menu-fixed')
   }
}

/*-----------------------------------------------*\
         OBJETO: TarjetaDetalleHallazgo
\*-----------------------------------------------*/

function TarjetaDetalleHallazgo(){

   this.$id_titulo = $('#id_titulo')
   this.$id_requisito_referencia = $('#id_requisito_referencia')
   this.$id_descripciones = $('#id_descripciones')
   this.$id_tipo_hallazgo = $('#id_tipo_hallazgo')
   this.$id_observaciones = $('#id_observaciones')

  //  this.$id_boton_guardar_detalle_hallazgo = $('#id_boton_guardar_detalle_hallazgo')
   this.init_Components()
}
TarjetaDetalleHallazgo.prototype.init_Components = function () {

   this.$id_requisito_referencia.multiselect(this.get_ConfMultiSelect())
   this.$id_requisito_referencia.siblings("div.btn-group").find("ul.multiselect-container").addClass('nova-bootstrap-multiselect-width-ul')
   this.$id_descripciones.multiselect(this.get_ConfMultiSelect())
   this.$id_descripciones.siblings("div.btn-group").find("ul.multiselect-container").addClass('nova-bootstrap-multiselect-width-ul')
   this.$id_tipo_hallazgo.select2(appnova.get_ConfigSelect2())
}
TarjetaDetalleHallazgo.prototype.get_ConfMultiSelect = function () {

   return {

      enableFiltering: true,
      buttonWidth: '100%',
      numberDisplayed: 2,
      maxHeight: 150,
      nonSelectedText: "Sin Selección",
      allSelectedText: "Todo Seleccionado",
      nSelectedText: "Seleccionados",
      filterPlaceholder: "Buscar",
      disableIfEmpty: true,
   }
}

/*-----------------------------------------------*\
         OBJETO: Tarjeta Analisis Causa
\*-----------------------------------------------*/

function TarjetaAnalisisCausa() {

   this.toolbar_analisis_causa = new ToolBarAnalisisCausa()
   this.grid_analisis_causa = new GridAnalisisCausa()
}

/*-----------------------------------------------*\
         OBJETO: ToolBar Analisis Causa
\*-----------------------------------------------*/

function ToolBarAnalisisCausa() {

   popup_analisis = new PopupAnalisis()
}

/*-----------------------------------------------*\
         OBJETO: Grid Analisis Causa
\*-----------------------------------------------*/

function GridAnalisisCausa() {

   this.$id = $('#id_grid_analisis_causa')
   this.init_Events()
}
GridAnalisisCausa.prototype.init_Events = function () {

   this.$id.on("click", '.clickable-row', this.click_FilaGrid)
}
GridAnalisisCausa.prototype.click_FilaGrid = function () {

   $(this).addClass('nova-active-row').siblings().removeClass('nova-active-row')
}

/*-----------------------------------------------*\
         OBJETO: Popup Analisis Causa
\*-----------------------------------------------*/

function PopupAnalisis() {

   this.$id_titulo = $('#id_titulo')
   this.$id_metodologia = $('#id_metodologia')
   this.$id_causas = $('#id_causas')
   this.$id_imagen = $('#id_imagen_analisis')
   this.$id_boton = $('#id_boton_analisis_causas')
   this.init_Components()
}
PopupAnalisis.prototype.init_Components = function () {

   this.$id_metodologia.select2(appnova.get_ConfigSelect2())
   this.$id_imagen.fileinput(this.get_ConfigFileInput())
}
PopupAnalisis.prototype.get_ConfigFileInput = function () {

   return {

          uploadUrl: "una/url/donde/se/subira/",
          uploadAsync: false,
          minFileCount: 2,
          maxFileCount: 5,
          overwriteInitial: false,
          language:"es",
          initialPreview: [
             "/static/images/referenciavisual/documento.jpg",
             "/static/images/referenciavisual/1.jpg",
             "/static/images/referenciavisual/2.jpg",
             "/static/images/referenciavisual/3.jpg",
          ],
          initialPreviewAsData: true,
          initialPreviewFileType: 'image',
          initialPreviewConfig: [
            {  caption: "Documento.jpg", size: 827000, url: "/file-upload-batch/2", key: 1  },
            {  caption: "1.jpg", size: 827000, url: "/file-upload-batch/2", key: 2  },
            {  caption: "2.jpg", size: 827000, url: "/file-upload-batch/2", key: 3  },
            {  caption: "3.jpg", size: 827000, url: "/file-upload-batch/2", key: 4  },
          ],
          purifyHtml: true,
     }
}

/*-----------------------------------------------*\
         OBJETO: Tarjeta Plan Accion
\*-----------------------------------------------*/

function TarjetaPlanAccion() {

   this.toolbar_plan_accion = new ToolBarPlanAccion()
   this.grid_plan_accion = new GridPlanAccion()
}

/*-----------------------------------------------*\
         OBJETO: ToolBar Plan Accion
\*-----------------------------------------------*/

function ToolBarPlanAccion() {

   popup_actividad = new PopupActividad()
}

/*-----------------------------------------------*\
         OBJETO: Grid Plan Accion
\*-----------------------------------------------*/

function GridPlanAccion() {

   popup_acciones = new PopupAcciones()
  //  popup_editarA = new PopupEditarA()
   this.$id_grid_plan_accion = $('#id_grid_plan_accion')
   this.init_Events()
}
GridPlanAccion.prototype.init_Events = function () {

   this.$id_grid_plan_accion.on("click", '.clickable-row', this.click_FilaGrid)
}
GridPlanAccion.prototype.click_FilaGrid = function () {

   $(this).addClass('nova-active-row').siblings().removeClass('nova-active-row')
}

/*-----------------------------------------------*\
         OBJETO: Popup Actividad
\*-----------------------------------------------*/

function PopupActividad() {

   this.$id_actividad = $('#id_actividad')
   this.$id_responsable = $('#id_responsable')
   this.$id_fecha_programada = $('#id_fecha_programada')
   this.$id_fecha_programada_group = $('#id_fecha_programada_group')
   this.init_Components()
}
PopupActividad.prototype.init_Components = function () {

   this.$id_responsable.select2(appnova.get_ConfigSelect2())
   this.$id_fecha_programada.mask(
      "9999-99-99",
      {
         placeholder:"aaaa/mm/dd"
      }
   )
   this.$id_fecha_programada_group.datetimepicker(this.get_DateTimePickerConfig())
}
PopupActividad.prototype.get_DateTimePickerConfig = function () {
   return {
      autoclose: true,
      orientation: "bottom left",
      minViewMode: 2,
      format: "yyyy-mm-dd",
   }
}

/*-----------------------------------------------*\
         OBJETO: popup acciones
\*-----------------------------------------------*/

function PopupAcciones () {

   popup_seguimiento_plan = new PopupSeguimientoPlan()
   popup_evaluacion_plan = new PopupEvaluacionPlan()
   this.$id_tarjeta_acciones = $('#id_tarjeta_acciones')
   this.$id_boton_evaluacion_eficacia = $('#id_boton_evaluacion_eficacia')
   this.$id_boton_seguimiento_plan = $('#id_boton_seguimiento_plan')
   this.init_Events()
}
PopupAcciones.prototype.init_Events = function () {

   this.$id_boton_seguimiento_plan.on("click", this, this.click_BotonSeguimientoPlan )
   this.$id_boton_evaluacion_eficacia.on("click", this, this.click_BotonEvaluacion)
}
PopupAcciones.prototype.click_BotonSeguimientoPlan = function (e) {

   e.preventDefault()
   popup_seguimiento_plan.$id.on('shown.bs.modal', function(){
      $("body").addClass("modal-open")
      $("html").addClass("be-modal-open")
   })
   e.data.$id_tarjeta_acciones.modal('hide')
}
PopupAcciones.prototype.click_BotonEvaluacion = function (e) {

   e.preventDefault()
   popup_evaluacion_plan.$id.on('shown.bs.modal', function(){
      $("body").addClass("modal-open")
      $("html").addClass("be-modal-open")
   })
   e.data.$id_tarjeta_acciones.modal('hide')
}

/*-----------------------------------------------*\
         OBJETO: popup seguimiento plan
\*-----------------------------------------------*/

function PopupSeguimientoPlan () {

   this.$id = $('#id_tarjeta_seguimiento_plan')
   this.$id_resultado_seguimiento = $('#id_resultado_seguimiento')
   this.$id_fecha_seguimiento_group = $('#id_fecha_seguimiento_group')
   this.$id_fecha_seguimiento = $('#id_fecha_seguimiento')
   this.$id_imagen = $('#id_imagen_seguimiento_plan')
   this.init_Components()
}
PopupSeguimientoPlan.prototype.init_Components = function () {

   this.$id_fecha_seguimiento.mask(
      "9999-99-99",
      {
         placeholder:"aaaa/mm/dd"
      }
   )
   this.$id_fecha_seguimiento_group.datetimepicker(this.get_DateTimePickerConfig())
   this.$id_imagen.fileinput(this.get_ConfigFileInput())
}
PopupSeguimientoPlan.prototype.get_DateTimePickerConfig = function () {

  return {
      autoclose: true,
      orientation: "bottom left",
      minViewMode: 2,
      format: "yyyy-mm-dd",
   }
}
PopupSeguimientoPlan.prototype.get_ConfigFileInput = function () {
   return {
          uploadUrl: "una/url/donde/se/subira/",
          uploadAsync: false,
          minFileCount: 2,
          maxFileCount: 5,
          overwriteInitial: false,
          language:"es",
          initialPreview: [
             "/static/images/referenciavisual/documento.jpg",
             "/static/images/referenciavisual/1.jpg",
          ],
          initialPreviewAsData: true,
          initialPreviewFileType: 'image',
          initialPreviewConfig: [
            {  caption: "Documento.jpg", size: 827000, url: "/file-upload-batch/2", key: 1  },
            {  caption: "1.jpg", size: 827000, url: "/file-upload-batch/2", key: 2  },
          ],
          purifyHtml: true,
     }
}

/*-----------------------------------------------*\
         OBJETO: popup evaluacion plan
\*-----------------------------------------------*/

function PopupEvaluacionPlan () {

   this.$id = $('#id_tarjeta_evaluacion')
   this.$id_resultado = $('#id_resultado_plan_eval')
   this.$id_resultado_evaluacion = $('#id_resultado_evaluacion_plan_eval')
   this.$id_fecha_evaluacion = $('#id_fecha_evaluacion_plan_eval')
   this.$id_fecha_evaluacion_group = $('#id_fecha_evaluacion_group')
   this.$id_criterio_decision = $('#id_criterio_decision_plan_eval')
   this.$id_imagen = $('#id_imagen_plan_eval')
   this.init_Components()
}
PopupEvaluacionPlan.prototype.init_Components = function () {

   this.$id_fecha_evaluacion.mask(
      "9999-99-99",
      {
         placeholder:"aaaa/mm/dd"
      }
   )
   this.$id_fecha_evaluacion_group.datetimepicker(this.get_DateTimePickerConfig())
   this.$id_imagen.fileinput(this.get_ConfigFileInput())
}
PopupEvaluacionPlan.prototype.get_ConfigFileInput = function () {

   return {

          uploadUrl: "una/url/donde/se/subira/",
          uploadAsync: false,
          minFileCount: 2,
          maxFileCount: 5,
          overwriteInitial: false,
          language:"es",
          initialPreview: [
             "/static/images/referenciavisual/documento.jpg",
             "/static/images/referenciavisual/1.jpg",
             "/static/images/referenciavisual/2.jpg",
             "/static/images/referenciavisual/3.jpg",
          ],
          initialPreviewAsData: true,
          initialPreviewFileType: 'image',
          initialPreviewConfig: [
            {  caption: "Documento.jpg", size: 827000, url: "/file-upload-batch/2", key: 1  },
            {  caption: "1.jpg", size: 827000, url: "/file-upload-batch/2", key: 2  },
            {  caption: "2.jpg", size: 827000, url: "/file-upload-batch/2", key: 3  },
            {  caption: "3.jpg", size: 827000, url: "/file-upload-batch/2", key: 4  },
          ],
          purifyHtml: true,
     }
}
PopupEvaluacionPlan.prototype.get_DateTimePickerConfig = function () {
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

// function PopupEditarA() {
//
//     this.$id_evidencia = $('#id_evidencia')
//     this.$id_plan_observaciones = $('#id_plan_observaciones')
//     this.init_Components()
// }
// PopupEditarA.prototype.init_Components = function () {
//
// }

/*-----------------------------------------------*\
         OBJETO: Tarjeta Evidencia
\*-----------------------------------------------*/

function TarjetaEvidencia() {

   this.toolbar_evidencia = new ToolBarEvidencia()
   this.grid_evidencia = new GridEvidencia()
}

/*-----------------------------------------------*\
         OBJETO: ToolBar Evidencia
\*-----------------------------------------------*/

function ToolBarEvidencia() {

   popup_evidencia = new PopupEvidencia()
}

/*-----------------------------------------------*\
         OBJETO: Grid Evidencia
\*-----------------------------------------------*/

function GridEvidencia() {

   this.$id_grid_evidencia = $('#id_grid_evidencia')
   this.init_Events()
}
GridEvidencia.prototype.init_Events = function () {

   this.$id_grid_evidencia.on("click", '.clickable-row', this.click_FilaGrid)
}
GridEvidencia.prototype.click_FilaGrid = function () {

   $(this).addClass('nova-active-row').siblings().removeClass('nova-active-row')
}

/*-----------------------------------------------*\
         OBJETO: popup evidencia
\*-----------------------------------------------*/

function PopupEvidencia () {

   this.$id_titulo_evidencia = $('#id_titulo_evidencia')
   this.$id_observacion = $('#id_observacion')
   this.$id_imagen_evidencia = $('#id_imagen_evidencia')
   this.init_Components()
}
PopupEvidencia.prototype.init_Components = function () {

   this.$id_imagen_evidencia.fileinput(this.get_ConfigFileInput())
}
PopupEvidencia.prototype.get_ConfigFileInput = function () {
   return {
          uploadUrl: "una/url/donde/se/subira/",
          uploadAsync: false,
          minFileCount: 2,
          maxFileCount: 5,
          overwriteInitial: false,
          language:"es",
          initialPreview: [
             "/static/images/referenciavisual/documento.jpg",
             "/static/images/referenciavisual/1.jpg",
             "/static/images/referenciavisual/2.jpg",
             "/static/images/referenciavisual/3.jpg",
          ],
          initialPreviewAsData: true,
          initialPreviewFileType: 'image',
          initialPreviewConfig: [
            {  caption: "Documento.jpg", size: 827000, url: "/file-upload-batch/2", key: 1  },
            {  caption: "1.jpg", size: 827000, url: "/file-upload-batch/2", key: 2  },
            {  caption: "2.jpg", size: 827000, url: "/file-upload-batch/2", key: 3  },
            {  caption: "3.jpg", size: 827000, url: "/file-upload-batch/2", key: 4  },
          ],
          purifyHtml: true,
     }
}
