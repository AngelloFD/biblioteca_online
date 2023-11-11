$(document).ready(function(){
  $(".add-to-cart").click(function(){
    var button = $(this);  // Guarda una referencia al botón
    var isbnLibro = button.data('isbn-libro');
    $.get("/add_book/", {isbn_libro: isbnLibro}, function(data){
      $(".badge").text(data.num_items);
      if (data.in_cart) {
        button.text("Libro en bandeja");  // Actualiza el texto del botón
      }
    });
  });
});
