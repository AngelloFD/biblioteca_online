$(document).ready(function(){
  function actualizarCarrito() {
    $.ajax({
        url: "/print_carrito/" + new Date().getTime(),  
        type: "GET",
        dataType: "json",
        success: function(data) {
            var carritoTableBody = $("#carrito_table tbody");
            carritoTableBody.empty();  
            $.each(data.carrito_detalle, function(index, item) {
                var nuevaFila = $("<tr>")
                    .append($("<td>").text(item.isbn))
                    .append($("<td>").text(item.titulo))
                    .append($("<td>").html('<a  href="#" class="eliminar-libro" data-isbn="' + item.isbn + '">Eliminar</a>'));
                carritoTableBody.append(nuevaFila);
            });
        },
        error: function(error) {
            console.error("Error al obtener datos del carrito: ", error);
        }
    });
  }

  $(".eliminar-libro").click(function(){
    var button = $(this);
    var isbnLibro = button.data('isbn-libro');
    $.get("/eliminar_libro/", {isbn_libro: isbnLibro}, function(data){
      $(".badge").text(data.num_items);
      actualizarCarrito();
    });
  });

  $(".add-to-cart").click(function(){
    var button = $(this);
    var isbnLibro = button.data('isbn-libro');
    
    $.get("/add_book/", {isbn_libro: isbnLibro}, function(data){
      if (data.in_cart) {
        button.text("Libro en bandeja");  // Actualiza el texto del botón
        button.removeClass("btn-outline-dark").addClass("btn-outline-primary disabled");
      }

      $(".badge").text(data.num_items);
      actualizarCarrito();
    });
  });

  $('.actualizar_contenido_btn').click(function() {
    var url = window.location.href; 
    $('.offcanvas-body').load(url + ' .offcanvas-body > *');
    actualizarCarrito();
  });

  $('.limpiar-boton').click(function(){

  });
  actualizarCarrito();
});
