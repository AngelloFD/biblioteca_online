/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
$(document).ready(function(){
   $(".add-to-cart").click(function(){
     var isbnLibro = $(this).data('isbn-libro');
     $.get("/add_book/", {isbn_libro: isbnLibro}, function(data){
       $(".badge").text(data.num_items);
     });
   });
 });