$("#textInput").click(function(){

    var formData = $("form").serialize();
     $.post("/",{data:formData},function(val){

      });
    });