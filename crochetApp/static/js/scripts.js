$(document).ready(function() {
    $('.all').click(function(){
        $('.allProducts').animate( {
            width: 'toggle'
        })
    })
    $('.showForm').click(function(){
        $('.categoryForm').animate( {
            width: 'toggle'
        })
    })
    $('.showProdForm').click(function(){
        $('.productForm').animate( {
            width: 'toggle'
        })
    })
})