//MPC
        $(function() {
			dialogSet = $( "#dialog-setpoint" ).dialog({
				autoOpen: false,
				modal: true,
				width: 808,
				height: 520,
				left: 300,
				top: 200,
				buttons: {
				"Save changes":
					function() {
                        //create json from values
                        var params_json = {
                            N: $("#Np").val(),
                            target: $("#target_p").val(),
                            step: $("#step_p").val(),
                            end: $("#end_p").val()
                        };

                        //pass json to field to be read by the view
                        $("#id_mod-method_params").val( JSON.stringify(params_json) );
                        $("#id_mod-method").val('CloseLoop-MPC');

						dialogSet.dialog( "close" );
					}
				},
			});

		});



        function openloop_send_vals(){
            //create the lists
            a = $('#N_int').val();
            var list_dose=[]
            var list_time=[]
            for( var i=0; i<a ;i++) {
                 if ($('#txtbox'+i).length){
                    list_dose[i]=$('#txtbox'+i).val()
                    var option_result = $('#txt'+i).val();
                    var option_array=option_result.split("-");
                    list_time[i] = option_array[0];
                    }
            }

            //create json from values
            var params_json = {
                total_time: $("#Time").val(),
			    total_N: a,
                dose: list_dose,
                time: list_time
			}

            //pass json to field to be read by the view
            $("#id_mod-method_params").val( JSON.stringify(params_json) );
        }
        //check if form is valid
        function check(){
             var a = document.getElementById('N_int').value;
             var t = $('#Time').val();
             var prev="0";
             var er=0;
             var list_time=[]
             var list_time2=[]
              for( var i=0; i<a ;i++) {
                if ($('#txtbox'+i).length){
                    var option_result = $('#txt'+i).val();
                    var option_array=option_result.split("-");
                    list_time[i] = option_array[0];
                    list_time2[i] = option_array[1];

                    if (i==0){
                        if (list_time[i] =! "0"){
                            er=1;
                        }
                        else{
                            var prev="0";
                        }
                    }
                    else{
                    prev= list_time2[i-1]
                    if(list_time[i] == prev){
                        prev= list_time2[i]

                    }
                    else{
                        er=1;

                    }
                    if (i == a-1){

                        if(list_time2[i] =! t){
                            er=1;
                        }
                    }
                    }

                  }
                }
                if(er==1){
                alert('Wrong values')
                }
                else
                {
                    $("#id_mod-method").val('OpenLoop');
                    dialogOpen.dialog( "close" );
                }

            }

        $(function() {
			dialogOpen = $( "#dialog-open" ).dialog({
				autoOpen: false,
				modal: true,
				width: 808,
				height: 520,
				left: 300,
				top: 200,
				buttons: {
				"Save changes":
					function() {
						openloop_send_vals();
						check();


					}
				},
			});

		});


