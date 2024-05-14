$(document).ready(function () {
  $(".btn-edit").on("click", function () {
    var cultivoId = $(this).data("id");
    var url = "{% url 'cultivos_iw:edit' 0 %}".replace("0", cultivoId);
    $.ajax({
      url: url,
      type: "GET",
      success: function (response) {
        $("#editarCultivoModal .modal-body").html(response.modal_content);
      },
    });
  });
});
