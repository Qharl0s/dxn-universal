$(function(){
    $('.bandera_a').click(function(e){
        e.preventDefault();
        $('.bandera_a').removeClass('bandera_activa').css('width','100%');
        $(this).addClass('bandera_activa').animate({
            width: "90px"
        }, {
            duration: 500,
            easing: "linear",
            complete: function () {}
        });
        $('.titulo_prod').html($(this).data('pais'));
        filtrar_productos();
    });
    $('.categoria').radiocharm();
    $('.categoria').click(function(){
        filtrar_productos();
    });

    /** Filtrar Productos */
    function filtrar_productos(){
        var pais = $('.bandera_activa').data('pais');
        if(pais === undefined)
            pais = "";
        
        var categoria='';
        if(typeof $('.label-radiocharm.active').children().next().next()[0] !='undefined')
            categoria = $('.label-radiocharm.active').children().next().next()[0].value;
        $('.producto_li').hide();
        $(".producto_li").each(function(){
            if($(this).data('categoria') == categoria && $(this).data('paises').indexOf(pais)>=0)
                $(this).fadeIn(900);
        });
    }

    filtrar_productos();
    /* Iconos */

    $('.leer_mas').click(function(){
        if($(this).hasClass('fa-angle-double-right'))
            $(this).removeClass('fa-angle-double-right').addClass('fa-angle-double-up').parent().prev().css('overflow','auto').css('display','block');
        else
            $(this).removeClass('fa-angle-double-up').addClass('fa-angle-double-right').parent().prev().css('overflow','hidden').css('display','-webkit-box');
    });

    $(".card").hover(
        function () {
            $(this).addClass("shadow-lg");
        },
        function () {
            $(this).removeClass("shadow-lg");
        }
    );
    
    $('.open-modal').click(function(){
        $('#plan').val($(this).data('plan'));
        $('.modal').show();
    });

    $('.close-modal').click(function(){
		$('.modal').hide();
	});
});