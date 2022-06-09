$(document).ready(function () {
    $('.faq-item__question').click(function () {
        if ($(this).parent().hasClass('active')) {
            $(this).parent().removeClass('active');
        } else {
            $('.faq-item').removeClass('active');
            $(this).parent().addClass('active');
        }
    });
});