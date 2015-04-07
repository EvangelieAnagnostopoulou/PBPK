//Create additional organs

           var counter = 1;
            var limit = 6;
            //Add an additional organ and display pop up window
            function addInput(divName){
                 if (counter == limit)  {
                      alert("You have reached the limit of adding " + (counter-1) + " inputs");
                 }
                 else if (counter == 1) {

                    $(function() {
                        dialogOrgan1Cr = $( "#dialog-organ1create" ).dialog({
                            autoOpen: false,
                            modal: true,
                            width: 708,
                            height: 520,
                            left: 300,
                            top: 200,
                            buttons: {
                            "Save changes":
                                function() {

                                    $("#id_mod-organ" + counter + "_flow_factor").val( $("#org1_f_fc").val() );
                                    $("#id_mod-organ" + counter + "_volume_fraction").val( $("#org1_v_fc").val() );
                                    $("#id_mod-blood_organ" + counter + "_fraction").val( $("#org1_b_fc").val() );

                                    $("#organ1").val($("#org1c").val() );
                                    $("#id_mod-organ1_name").val($("#organ1").val() );

                                    document.getElementById('organ1').style.display = 'block';
                                    counter++;
                                    $('#counter_id').val(+counter);
                                   $('#blood').animate({height: '+=50'}, 500);
                                   $('#Blood2').animate({height: '+=50'}, 500);
                                   $('#Create_model').animate({top: '+=50'}, 500);
                                   $('#Add_organs').animate({top: '+=50'}, 500);
                                   $('#removeButton').animate({top: '+=50'}, 500);
                                   $('#organ1').css('background-color','#16A085');
                                   $('#organ1').data('clicked', true);
                                   if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                                        canvas.style.display="block";
                                        neworgan($("#div-placental").position().left,$("#div-placental").position().top);
                                    }

                                   /* $('#metabolise').click(function() {
                                    //Now just reference this button and change CSS
                                    alert('hi');
                                    });*/

                                    $("#org1_f_f").val( $("#id_mod-organ1_flow_factor").val() );
                                    $("#org1_v_f").val( $("#id_mod-organ1_volume_fraction").val() );
                                    $("#org1_b_f").val( $("#id_mod-blood_organ1_fraction").val() );
                                    $("#org1").val( $("#id_mod-organ1_name").val() );
                                    dialogOrgan1Cr.dialog( "close" );

                                }
                            },
                        });
                    });

                    dialogOrgan1Cr.dialog( "open" );

                 }
                 else if (counter == 2) {

                      $(function() {
                        dialogOrgan1Cr = $( "#dialog-organ2create" ).dialog({
                            autoOpen: false,
                            modal: true,
                            width: 708,
                            height: 520,
                            left: 300,
                            top: 200,
                            buttons: {
                            "Save changes":
                                function() {
                                    $("#id_mod-organ" + counter + "_flow_factor").val( $("#org2_f_fc").val() );
                                    $("#id_mod-organ" + counter + "_volume_fraction").val( $("#org2_v_fc").val() );
                                    $("#id_mod-blood_organ" + counter + "_fraction").val( $("#org2_b_fc").val() );
                                    /*$("#p_organ" + counter).val( $("#p_org2c").val() );
                                    $("#pi_organ" + counter ).val( $("#pi_org2c").val() );
                                    var nam=$("#org2c").val();
                                    //Get the type of the organ
                                   $("#organ" + counter + "type").val( $('#dialog-organ2create').find('input:checked').val() );
                                   //If type of organ is non metabolising
                                   if( $("#organ" + counter + "type").val() == "met"){
                                        //Get the selected option(constains) from pop up window
                                        $('select[name="constains2" ]').val($('select[name="const"]').val() );

                                        }*/

                                   $("#organ" + counter).val($("#org2c").val() );
                                   $("#id_mod-organ2_name").val($("#org2c").val() );
                                    document.getElementById('organ' + counter).style.display = 'block';

                                  counter++;
                                  $('#counter_id').val(+counter);
                                   $('#blood').animate({height: '+=50'}, 500);
                                   $('#Blood2').animate({height: '+=50'}, 500);
                                   $('#Create_model').animate({top: '+=50'}, 500);
                                   $('#Add_organs').animate({top: '+=50'}, 500);
                                   $('#removeButton').animate({top: '+=50'}, 500);
                                    $('#organ2').css('background-color','#16A085');
                                    $('#organ2').data('clicked', true);
                                    if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                                        canvas.style.display="block";
                                        neworgan($("#div-placental").position().left,$("#div-placental").position().top+50);
                                    }

                                    //organ_click();
                                   /* $('#metabolise').click(function() {
                                    //Now just reference this button and change CSS
                                    alert('hi');
                                    });*/

                                    $("#org2_f_f").val( $("#id_mod-organ2_flow_factor").val() );
                                    $("#org2_v_f").val( $("#id_mod-organ2_volume_fraction").val() );
                                    $("#org2_b_f").val( $("#id_mod-blood_organ2_fraction").val() );

                                    dialogOrgan1Cr.dialog( "close" );

                                }
                            },
                        });
                    });

                    dialogOrgan1Cr.dialog( "open" );

                 }
                 else if (counter == 3) {

                      $(function() {
                        dialogOrgan1Cr = $( "#dialog-organ3create" ).dialog({
                            autoOpen: false,
                            modal: true,
                            width: 708,
                            height: 520,
                            left: 300,
                            top: 200,
                            buttons: {
                            "Save changes":
                                function() {
                                    $("#id_mod-organ" + counter + "_flow_factor").val( $("#org3_f_fc").val() );
                                    $("#id_mod-organ" + counter + "_volume_fraction").val( $("#org3_v_fc").val() );
                                    $("#id_mod-blood_organ" + counter + "_fraction").val( $("#org3_b_fc").val() );

                                   $("#organ3").val($("#org3c").val() );
                                   $("#id_mod-organ3_name").val($("#org3c").val() );
                                    document.getElementById('organ3').style.display = 'block';

                                  counter++;
                                  $('#counter_id').val(+counter);
                                   $('#blood').animate({height: '+=50'}, 500);
                                   $('#Blood2').animate({height: '+=50'}, 500);
                                   $('#Create_model').animate({top: '+=50'}, 500);
                                   $('#Add_organs').animate({top: '+=50'}, 500);
                                   $('#removeButton').animate({top: '+=50'}, 500);
                                   $('#organ3' ).css('background-color','#16A085');
                                   $('#organ3').data('clicked', true);
                                    if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                                        canvas.style.display="block";
                                        neworgan($("#div-placental").position().left,$("#div-placental").position().top+100);
                                    }
                                    $("#org3_f_f").val( $("#id_mod-organ3_flow_factor").val() );
                                    $("#org3_v_f").val( $("#id_mod-organ3_volume_fraction").val() );
                                    $("#org3_b_f").val( $("#id_mod-blood_organ3_fraction").val() );

                                    dialogOrgan1Cr.dialog( "close" );

                                }
                            },
                        });
                    });

                    dialogOrgan1Cr.dialog( "open" );

                 }

                 else if (counter == 4) {

                      $(function() {
                        dialogOrgan1Cr = $( "#dialog-organ4create" ).dialog({
                            autoOpen: false,
                            modal: true,
                            width: 708,
                            height: 520,
                            left: 300,
                            top: 200,
                            buttons: {
                            "Save changes":
                                function() {
                                    $("#id_mod-organ" + counter + "_flow_factor").val( $("#org4_f_fc").val() );
                                    $("#id_mod-organ" + counter + "_volume_fraction").val( $("#org4_v_fc").val() );
                                    $("#id_mod-blood_organ" + counter + "_fraction").val( $("#org4_b_fc").val() );

                                   $("#organ4").val($("#org4c").val() );
                                   $("#id_mod-organ4_name").val($("#org4c").val() );
                                    document.getElementById('organ4').style.display = 'block';

                                  counter++;
                                  $('#counter_id').val(+counter);
                                   $('#blood').animate({height: '+=50'}, 500);
                                   $('#Blood2').animate({height: '+=50'}, 500);
                                   $('#Create_model').animate({top: '+=50'}, 500);
                                   $('#Add_organs').animate({top: '+=50'}, 500);
                                   $('#removeButton').animate({top: '+=50'}, 500);
                                   $('#organ4' ).css('background-color','#16A085');
                                   $('#organ4').data('clicked', true);
                                    if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                                        canvas.style.display="block";
                                        neworgan($("#div-placental").position().left,$("#div-placental").position().top+150);
                                    }

                                    $("#org4_f_f").val( $("#id_mod-organ4_flow_factor").val() );
                                    $("#org4_v_f").val( $("#id_mod-organ4_volume_fraction").val() );
                                    $("#org4_b_f").val( $("#id_mod-blood_organ4_fraction").val() );

                                    dialogOrgan1Cr.dialog( "close" );

                                }
                            },
                        });
                    });

                    dialogOrgan1Cr.dialog( "open" );

                 }
                 else if (counter == 5) {

                      $(function() {
                        dialogOrgan1Cr = $( "#dialog-organ5create" ).dialog({
                            autoOpen: false,
                            modal: true,
                            width: 708,
                            height: 520,
                            left: 300,
                            top: 200,
                            buttons: {
                            "Save changes":
                                function() {
                                    $("#id_mod-organ" + counter + "_flow_factor").val( $("#org5_f_fc").val() );
                                    $("#id_mod-organ" + counter + "_volume_fraction").val( $("#org5_v_fc").val() );
                                    $("#id_mod-blood_organ" + counter + "_fraction").val( $("#org5_b_fc").val() );

                                   $("#organ5").val($("#org5c").val() );
                                   $("#id_mod-organ5_name").val($("#org5c").val() );
                                    document.getElementById('organ5').style.display = 'block';

                                  counter++;
                                  $('#counter_id').val(+counter);
                                   $('#blood').animate({height: '+=50'}, 500);
                                   $('#Blood2').animate({height: '+=50'}, 500);
                                   $('#Create_model').animate({top: '+=50'}, 500);
                                   $('#Add_organs').animate({top: '+=50'}, 500);
                                   $('#removeButton').animate({top: '+=50'}, 500);
                                   $('#organ5' ).css('background-color','#16A085');
                                   $('#organ5').data('clicked', true);
                                   if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                                        canvas.style.display="block";
                                        neworgan($("#div-placental").position().left,$("#div-placental").position().top+200);
                                    }

                                    $("#org5_f_f").val( $("#id_mod-organ5_flow_factor").val() );
                                    $("#org5_v_f").val( $("#id_mod-organ5_volume_fraction").val() );
                                    $("#org5_b_f").val( $("#id_mod-blood_organ5_fraction").val() );

                                    dialogOrgan1Cr.dialog( "close" );

                                }
                            },
                        });
                    });

                    dialogOrgan1Cr.dialog( "open" );

                 }



            }
