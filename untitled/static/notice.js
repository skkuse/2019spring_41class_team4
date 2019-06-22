$(document).ready(function(){
	var count = 0;
	$("#notification-dropdown").hide();
	$("#bellClick").click(function(){
				  $("#notification-dropdown").toggle();
					var count = 0;
					$("#notifications-count").html(count);
					$("#dd-notifications-count").html(count);
	});
	$(".body-image").click(function(){
		  $("#notification-dropdown").hide();
	})
	$(".searchbox-wrapper").click(function() {
		$("#notification-dropdown").hide();
	})

	var data = [
    {"name":"bob32@gmail.com","status" :"down voted"}
];
console.log(data);
	var notification = '';
	setInterval(function(){
    //code goes here that will be run every 5 seconds.
		for(var i=0;i<data.length;i++){
			var cnt = document.getElementById("notifications-count").innerHTML;
		console.log(cnt);
			if(cnt==0){
				count = 0;
			}
			count +=1;
			if(data.length > 0){
				notification += "<div class='notification new'><div class='notification-text'><span class='highlight'>"+" "+data[i].name+"</span>"+" "+data[i].status+"</div></div>";
			}
		}
		 $(".dropdown-body").prepend(notification);
		 $("#notifications-count").html(count);
		 $("#dd-notifications-count").html(count);

}, 5000);





});
