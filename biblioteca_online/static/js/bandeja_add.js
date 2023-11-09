$(document).ready(function(){
   $(".add-to-cart").click(function(){
     var isbnLibro = $(this).data('isbn-libro');
     $.get("/add_book/", {isbn_libro: isbnLibro}, function(data){
       $(".badge").text(data.num_items);
     });
   });
 });