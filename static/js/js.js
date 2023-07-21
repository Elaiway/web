// JavaScript Document
 function changing(id){
      console.log(id);
  
  
 var url = "shoucang.php";
 var data = {id:id};
 $.ajax({
  type : "get",
  url : url,
  data : data,
  timeout:1000,
  success:function(dates){
 
       alert(dates.msg);
  },
 
 
 });
  }

  