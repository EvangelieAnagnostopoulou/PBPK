$(function() {
    $('#Create_model').bind('click', function(e)
                    {
                        $("#loading").show();
                        $('.example-image').remove();
                        $('.example-image-link').remove();

                        var url = '';
                        if (ModelForm.default) {
                            if (ModelForm.tutorial) {
                                url = '/tutorial/';
                            } else {
                                url: '/default/';
                            }
                        }
                        else if (ModelForm.edit) {
                            url = '/edit_model/';
                        } else {
                            url = '/NewModel/';
                        }

                        $.ajax({
                            url: url,
                            type: 'POST',
                            data: {
                                csrfmiddlewaretoken: ModelForm.token,
                            },
                            cache: 'false',
                            success: function(data, textStatus, jqXHR) {
                                   //data=data.replace('data: test/png;base64', ' ')
                                   data=JSON.parse(data)
                                   $("#loading").hide();
                             }
                        });
                    });



// if user click the run buttom clicked "Create model" buttom
    $( "#run" ).on( "click", function() {
            $('#submit_id').val('Run');
            $('input[type=submit]').click();
			});

    //add class to form elements
    $(function() {
        $(".new-model-form input").addClass("form-control");
    });

    $(function() {
            var buttons;
			if (ModelForm.default) {
			    buttons = {
			        "OK":{
                        "class": 'btn-ok-residual',
				        text: "OK",
				        id: "residual-ok",
				        click: function() {
						    dialogResidual.dialog( "close" );
					    }
					}
				};
			} else {
			    buttons = {
			        "Save changes":{
				        text: "Save changes",
				        id: "res-sv",
					    click: function() {
						    $("#id_mod-blood_rest_fraction").val( $("#res_b_f").val() );

						    dialogResidual.dialog( "close" );
					    }
					}
				};
			}
			dialogResidual = $( "#dialog-residual" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: buttons
			});
		});

		$(function() {
		    var buttons;
		    if (ModelForm.default) {
		        buttons = {"OK":{
				    "class": 'btn-ok-skin',
				    text: "OK",
				    id: "skin-ok",
				    click: function() {
						dialogSkin.dialog( "close" );
					}
					}

		        }
		    }   else {
		        buttons = {"Save changes":{
				    text: "Save changes",
					click: function() {
						$("#id_mod-skin_flow_factor").val( $("#sk_f_f").val() );
						$("#id_mod-skin_volume_fraction").val( $("#sk_v_f").val() );
						$("#id_mod-blood_skin_fraction").val( $("#sk_b_f").val() );
						dialogSkin.dialog( "close" );
                        /*if(($("#id_mod-skin_flow_factor").val() != "0.0" || $("#id_mod-skin_volume_fraction").val() != "0.0" || $("#id_mod-blood_skin_fraction").val() != "0.0" || $("#id_dr-p_skin").val() != "0.0" || $("#id_dr-pi_skin").val() != "0.0") && ($("#id_mod-blood_volume_fraction").val() != "0.0" || $("#id_dr-pi_rbc").val() != "0.0" || $("#id_dr-pi_plasma").val() != "0.0") ){
                            canvas.style.display="block";
                            organ_dart($( "#skin" ));
                        }*/
					}
					}

		        }
		    }
			dialogSkin = $( "#dialog-skin" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: buttons

			});
		});

		$(function() {
		    var buttons;
		    if (ModelForm.default) {
		        buttons = {"OK":{
				    "class": 'btn-ok-kidney',
				    text: "OK",
				    id: "kidney-ok",
				    click: function() {
						dialogKidney.dialog( "close" );
					}
					}};
		    } else {
				buttons = {"Save changes":{
				    text: "Save changes",
				    id: "kidney-sv",
					click: function() {
						$("#id_mod-kidney_flow_factor").val( $("#kid_f_f").val() );
						$("#id_mod-kidney_volume_fraction").val( $("#kid_v_f").val() );
						$("#id_mod-blood_kidney_fraction").val( $("#kid_b_f").val() );
						dialogKidney.dialog( "close" );
                        /*if(($("#id_mod-kidney_flow_factor").val() != "0.0" || $("#id_mod-kidney_volume_fraction").val() != "0.0" || $("#id_mod-blood_kidney_fraction").val() != "0.0" || $("#id_dr-p_kidney").val() != "0.0" || $("#id_dr-pi_kidney").val() != "0.0") && ($("#id_mod-blood_volume_fraction").val() != "0.0" || $("#id_dr-pi_rbc").val() != "0.0" || $("#id_dr-pi_plasma").val() != "0.0")) {
                            canvas.style.display="block";
                            organ_dart($( "#kidney" ));
                        }*/
					}
					}};
			}

			dialogKidney = $( "#dialog-kidney" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: buttons
			});
		});

		$(function() {
		    var buttons;
		    if (ModelForm.default) {
		        buttons = {"OK":{
				    "class": 'btn-ok-bladder',
				    text: "OK",
				    id: "bladder-ok",
				    click: function() {
						dialogBladder.dialog( "close" );
					}
					}};
			} else {
			    buttons = {"Save changes":{
				    text: "Save changes",
					click: function() {
						$("#id_mod-bladder_flow_factor").val( $("#bl_f_f").val() );
						$("#id_mod-bladder_volume_fraction").val( $("#bl_v_f").val() );
						$("#id_mod-blood_bladder_fraction").val( $("#bl_b_f").val() );

						dialogBladder.dialog( "close" );
						/*if(($("#id_mod-bladder_flow_factor").val() != "0.0" || $("#id_mod-bladder_volume_fraction").val() != "0.0" || $("#id_mod-blood_bladder_fraction").val() != "0.0" || $("#id_dr-p_bladder").val() != "0.0" || $("#id_dr-pi_bladder").val() != "0.0") && ($("#id_mod-blood_volume_fraction").val() != "0.0" || $("#id_dr-pi_rbc").val() != "0.0" || $("#id_dr-pi_plasma").val() != "0.0")) {
                            canvas.style.display="block";
                            organ_dart($( "#bladder" ));
                        }*/
					}
				}};
			}

			dialogBladder = $( "#dialog-bladder" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: buttons
			});
		});


		$(function() {
		    var buttons;
		    if (ModelForm.default) {
		        buttons = {"OK":{
				    "class": 'btn-ok-liver',
				    text: "OK",
				    id: "liver-ok",
				    click: function() {
						dialogLiver.dialog( "close" );
					}
					}}
		    } else {
		        buttons = {
		            "Save changes": {
				    text: "Save changes",
					click : function() {
						$("#id_mod-liver_flow_factor").val( $("#liv_f_f").val() );
						$("#id_mod-liver_volume_fraction").val( $("#liv_v_f").val() );
						$("#id_mod-blood_liver_fraction").val( $("#liv_b_f").val() );

						dialogLiver.dialog( "close" );
						/*if(($("#id_mod-liver_flow_factor").val() != "0.0" || $("#id_mod-liver_volume_fraction").val() != "0.0" || $("#id_mod-blood_liver_fraction").val() != "0.0" || $("#id_dr-p_liver").val() != "0.0" || $("#id_dr-pi_liver").val() != "0.0") && ($("#id_mod-blood_volume_fraction").val() != "0.0" || $("#id_dr-pi_rbc").val() != "0.0" || $("#id_dr-pi_plasma").val() != "0.0")) {
                            canvas.style.display="block";
                            liver();
                        }*/
					}
					}
		        }
		    }

			dialogLiver = $( "#dialog-liver" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: buttons
			});
		});

		$(function() {
		    var buttons;
		    if (ModelForm.default) {
		        buttons = {
                    "blood-btn": {
				    "class": 'btn-ok-blood',
				    text: "OK",
				    id: "blood-ok",
				    click: function() {
						dialogBlood.dialog( "close" );
					}
					}
		        }
		    } else {
		        buttons = {
		            "Save changes": {
                    text: "Save changes",
                    id: "blood-sv",
                    click : function() {
						$("#id_mod-blood_volume_fraction").val( $("#blo_v_f").val() );
						dialogBlood.dialog( "close" );
					}
					}
		        }
		    }

			dialogBlood = $( "#dialog-blood" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: buttons
			});
		});

		$(function() {
		    var buttons;
		    if (ModelForm.default) {
		        buttons = {
		        "OK":{
				    "class": 'btn-ok-lung',
				    text: "OK",
				    id: "lung-ok",
				    click: function() {
						dialogLung.dialog( "close" );
					},
					}
		        }
		    } else {
		        buttons = {
		            "Save changes":{
				    text: "Save changes",
				    id: "lung-sv",
					click: function() {
						$("#id_mod-lung_flow_factor").val( $("#lg_f_f").val() );
						$("#id_mod-lung_volume_fraction").val( $("#lg_v_f").val() );
						$("#id_mod-blood_lung_fraction").val( $("#lg_b_f").val() );

						dialogLung.dialog( "close" );
					}
					}
		        }

		    }

			dialogLung = $( "#dialog-lung" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: buttons
			});
		});


		$(function() {
			dialogOrgan1 = $( "#dialog-organ1" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: {
				"Save changes":
					function() {
					    $("#id_mod-organ1_name").val( $("#org1").val() );
						$("#id_mod-organ1_flow_factor").val( $("#org1_f_f").val() );
						$("#id_mod-organ1_volume_fraction").val( $("#org1_v_f").val() );
						$("#id_mod-blood_organ1_fraction").val( $("#org1_b_f").val() );
						$("#organ1").val( $("#id_mod-organ1_name").val() );
						dialogOrgan1.dialog( "close" );

					}
				},
			});
		});

		$(function() {
			dialogOrgan2 = $( "#dialog-organ2" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: {
				"Save changes":
					function() {
					    $("#id_mod-organ2_name").val( $("#org2").val() );
						$("#id_mod-organ2_flow_factor").val( $("#org2_f_f").val() );
						$("#id_mod-organ2_volume_fraction").val( $("#org2_v_f").val() );
						$("#id_mod-blood_organ2_fraction").val( $("#org2_b_f").val() );
						$("#organ2").val( $("#id_mod-organ2_name").val() );
						dialogOrgan2.dialog( "close" );

					}
				},
			});
		});

		$(function() {
			dialogOrgan3 = $( "#dialog-organ3" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: {
				"Save changes":
					function() {
                        $("#id_mod-organ3_name").val( $("#org3").val() );
						$("#id_mod-organ3_flow_factor").val( $("#org1_f_f").val() );
						$("#id_mod-organ3_volume_fraction").val( $("#org1_v_f").val() );
						$("#id_mod-blood_organ3_fraction").val( $("#org1_b_f").val() );
						$("#organ3").val( $("#id_mod-organ3_name").val() );
						dialogOrgan3.dialog( "close" );

					}
				},
			});
		});

		$(function() {
			dialogOrgan4 = $( "#dialog-organ4" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: {
				"Save changes":
					function() {
					    $("#id_mod-organ4_name").val( $("#org4").val() );
						$("#id_mod-organ4_flow_factor").val( $("#org1_f_f").val() );
						$("#id_mod-organ4_volume_fraction").val( $("#org1_v_f").val() );
						$("#id_mod-blood_organ4_fraction").val( $("#org1_b_f").val() );
						$("#organ4").val( $("#id_mod-organ4_name").val() );
						dialogOrgan4.dialog( "close" );

					}
				},
			});
		});

		$(function() {
			dialogOrgan5 = $( "#dialog-organ5" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: {
				"Save changes":
					function() {
					    $("#id_mod-organ5_name").val( $("#org5").val() );
						$("#id_mod-organ5_flow_factor").val( $("#org1_f_f").val() );
						$("#id_mod-organ5_volume_fraction").val( $("#org1_v_f").val() );
						$("#id_mod-blood_organ5_fraction").val( $("#org1_b_f").val() );
						$("#organ5").val( $("#id_mod-organ5_name").val() );
						dialogOrgan5.dialog( "close" );

					}
				},
			});

	    if (!ModelForm.default) {
			dialogHeart = $( "#dialog-heart" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: {
				"Save changes":
					function() {
						$("#id_mod-heart_flow_factor").val( $("#h_f_f").val() );
						$("#id_mod-heart_volume_fraction").val( $("#h_v_f").val() );
						$("#id_mod-blood_heart_fraction").val( $("#h_b_f").val() );
						dialogHeart.dialog( "close" );
					}
				},
			});

			dialogMuscle = $( "#dialog-muscle" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: {"Save changes":
					function() {
						$("#id_mod-muscle_flow_factor").val( $("#m_f_f").val() );
						$("#id_mod-muscle_volume_fraction").val( $("#m_v_f").val() );
						$("#id_mod-blood_muscle_fraction").val( $("#m_b_f").val() );
						dialogMuscle.dialog( "close" );
					}
				}
			});

			dialogSpleen = $( "#dialog-spleen" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: {"Save changes":
					function() {
						$("#id_mod-spleen_flow_factor").val( $("#sp_f_f").val() );
						$("#id_mod-spleen_volume_fraction").val( $("#sp_v_f").val() );
						$("#id_mod-blood_spleen_fraction").val( $("#sp_b_f").val() );
						dialogSpleen.dialog( "close" );
					}
				}
			});

			dialogPlacental = $( "#dialog-placental" ).dialog({
				autoOpen: false,
				modal: true,
				width: 608,
				height: 320,
				left: 300,
				top: 200,
				buttons: {"Save changes":
					function() {
						$("#id_mod-placental_flow_factor").val( $("#pl_f_f").val() );
						$("#id_mod-placental_volume_fraction").val( $("#pl_v_f").val() );
						$("#id_mod-blood_placental_fraction").val( $("#pl_b_f").val() );
						dialogPlacental.dialog( "close" );
					}
				}
			});
		}
	});


//Add and remove organs from the model -->

        // Residual
        var checked_res=0;
        $("#residual").click(function(e) {

        if(checked_res==0) {
                //Now just reference this button and change CSS
                $(this).css('background-color','#16A085');
                $(this).data('clicked', true);
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    canvas.style.display="block";
                    organ_dart($( "#residual" ));
                }
                dialogResidual.dialog( "open" );
                checked_res=1;
        }
        else {

                if (ModelForm.default) {
                    dialogResidual.dialog( "open" );
                } else {
                    $("#dialog-confirm").html("Edit or Delete Residual?");

                    // Define the Dialog and its properties.
                    $("#dialog-confirm").dialog({
                        resizable: false,
                        modal: true,
                        title: "Residual",
                        height: 250,
                        width: 400,
                        buttons: {
                            "Delete": function () {
                                $(this).dialog('close');
                                delete_organ('residual');
                                //delete residual from model replacing its parameters with 0.0
                                $('#id_mod-blood_rest_fraction').val("0.0");
                                $('#id_dr-p_rest').val("0.0");
                                $('#id_dr-pi_rest').val("0.0");
                                checked_res=0;
                                //callback(true);
                            },
                            "Cancel": function () {
                                    $(this).dialog('close');
                                    //dialogSkin.dialog( "open" );
                                    checked_res=1;
                                    //callback(false);
                            },
                            "Edit": function () {
                                    $(this).dialog('close');
                                    dialogResidual.dialog( "open" );
                            }
                        }
                    });
                }

            }

        });

        // Skin
		var checked_sk=0;
		$('#skin').click(function(e) {

        //if skin is not selected open pop up window and add darts.
		    if(checked_sk==0){
                //Now just reference this button and change CSS
                $(this).css('background-color','#16A085');
                $(this).data('clicked', true);
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    canvas.style.display="block";
                    organ_dart($( "#skin" ));;
                    }
                dialogSkin.dialog( "open" );
                checked_sk=1;
            }
            //if skin is selected if user want delete skin from the model delete it.
            else{

                if (ModelForm.default) {
                    dialogSkin.dialog( "open" );
                } else {
                    $("#dialog-confirm").html("Edit or Delete Skin?");

                    // Define the Dialog and its properties.
                    $("#dialog-confirm").dialog({
                        resizable: false,
                        modal: true,
                        title: "Skin",
                        height: 250,
                        width: 400,
                        buttons: {
                            "Delete": function () {
                                $(this).dialog('close');
                                delete_organ('skin');
                                //delete skin from model replacing its parameters with 0.0
                                $('#id_mod-skin_flow_factor').val("0.0");
                                $('#id_mod-skin_volume_fraction').val("0.0");
                                $('#id_mod-blood_skin_fraction').val("0.0");
                                $('#id_dr-p_skin').val("0.0");
                                $('#id_dr-pi_skin').val("0.0");
                                checked_sk=0;
                                //callback(true);
                                },
                                "Cancel": function () {
                                    $(this).dialog('close');
                                    //dialogSkin.dialog( "open" );
                                    checked_sk=1;
                                    //callback(false);
                                },
                                "Edit": function () {
                                    $(this).dialog('close');
                                    dialogSkin.dialog( "open" );
                            }
                        }

                    });
                }
            }

		});

		//Kidney

		var checked_k=0;
		$('#kidney').click(function() {
		    if(checked_k==0){
                //Now just reference this button and change CSS
                $(this).css('background-color','#16A085');
                $(this).data('clicked', true);
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                canvas.style.display="block";
                organ_dart($( "#kidney" ));
                }
                dialogKidney.dialog( "open" );
                checked_k=1;
            }
             else{

                if (ModelForm.default) {
                    dialogKidney.dialog( "open" );
                } else {
                    $("#dialog-confirm").html("Edit or Delete Kidney?");

                    // Define the Dialog and its properties.
                    $("#dialog-confirm").dialog({
                        resizable: false,
                        modal: true,
                        title: "Kidney",
                        height: 250,
                        width: 400,
                        buttons: {
                            "Delete": function () {
                                $(this).dialog('close');
                                delete_organ('kidney');
                                $('#id_mod-kidney_flow_factor').val("0.0");
                                $('#id_mod-kidney_volume_fraction').val("0.0");
                                $('#id_mod-blood_kidney_fraction').val("0.0");
                                $('#id_dr-p_kidney').val("0.0");
                                $('#id_dr-pi_kidney').val("0.0");
                                $('#id_dr-k_kidney').val("0.0");
                                checked_k=0;
                                //callback(true);
                            },
                            "Cancel": function () {
                                    $(this).dialog('close');
                                    //dialogSkin.dialog( "open" );
                                    checked_k=1;
                                    //callback(false);
                            },
                            "Edit": function () {
                                    $(this).dialog('close');
                                    dialogKidney.dialog( "open" );
                            }
                        }
                    });
                }
             }
        });

        //Bladder

        var checked_bla=0;
		$('#bladder').click(function() {
		    if(checked_bla==0){
                //Now just reference this button and change CSS
                $(this).css('background-color','#16A085');
                $(this).data('clicked', true);
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                canvas.style.display="block";
                //organ_dart($( "#bladder" ));
                //var p3 = $( "#bladder" );
                organ_dart($( "#bladder" ));
                }
                dialogBladder.dialog( "open" );
                checked_bla=1;
            } else {
                if (ModelForm.default) {
                    dialogBladder.dialog( "open" );
                } else {
                    $("#dialog-confirm").html("Edit or delete Bladder?");

                    // Define the Dialog and its properties.
                    $("#dialog-confirm").dialog({
                        resizable: false,
                        modal: true,
                        title: "Bladder",
                        height: 250,
                        width: 400,
                        buttons: {
                            "Delete": function () {
                                $(this).dialog('close');
                                delete_organ('bladder');
                                $('#id_mod-bladder_flow_factor').val("0.0");
                                $('#id_mod-bladder_volume_fraction').val("0.0");
                                $('#id_mod-blood_bladder_fraction').val("0.0");
                                $('#id_dr-p_bladder').val("0.0");
                                $('#id_dr-pi_bladder').val("0.0");
                                checked_bla=0;
                                //callback(true);
                            },
                            "Cancel": function () {
                                $(this).dialog('close');
                                //dialogSkin.dialog( "open" );
                                checked_bla=1;
                                //callback(false);
                            },
                            "Edit": function () {
                                $(this).dialog('close');
                                dialogBladder.dialog( "open" );
                            }
                        }
                    });
                }
             }
		});

		//Liver

		var checked_liv=0;
		$('#liver').click(function() {
		    if(checked_liv==0){
                //Now just reference this button and change CSS
                $(this).css('background-color','#16A085');
                $(this).data('clicked', true);
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                canvas.style.display="block";
                liver();
                }
                dialogLiver.dialog( "open" );
                checked_liv=1;
            }
            else{
                if (ModelForm.default) {
                    dialogLiver.dialog( "open" );
                } else {
                    $("#dialog-confirm").html("Edit or Delete Liver?");

                    // Define the Dialog and its properties.
                    $("#dialog-confirm").dialog({
                        resizable: false,
                        modal: true,
                        title: "Liver",
                        height: 250,
                        width: 400,
                        buttons: {
                            "Delete": function () {
                                $(this).dialog('close');
                                delete_organ('liver');
                                $('#id_mod-liver_flow_factor').val("0.0");
                                $('#id_mod-liver_volume_fraction').val("0.0");
                                $('#id_mod-blood_liver_fraction').val("0.0");
                                $('#id_dr-p_liver').val("0.0");
                                $('#id_dr-pi_liver').val("0.0");
                                $('#id_dr-k_met').val("0.0");
                                $('#id_dr-k_bile').val("0.0");
                                checked_liv=0;
                                //callback(true);
                            },
                            "Cancel": function () {
                                    $(this).dialog('close');
                                    //dialogSkin.dialog( "open" );
                                    checked_liv=1;
                                    //callback(false);
                            },
                            "Edit": function () {
                                    $(this).dialog('close');
                                    dialogLiver.dialog( "open" );
                            }
                        }
                    });
                }
            }

		});

		//Blood

		var checked_bl=0;
		$('#blood').click(function() {

		    if(checked_bl==0){
		        add_blood('blood');
		        $("#Blood2").css('background-color','#16A085');
                dialogBlood.dialog( "open" );
		        checked_bl=1;
		    }
		    else{
                dialogBlood.dialog( "open" );
		    }

		});

		//Blood 2

		//var checked_bl2=0;
		$('#Blood2').click(function() {

		    if(checked_bl==0){
		        add_blood('Blood2');
		        $("#blood").css('background-color','#16A085');
		        dialogBlood.dialog( "open" );
		        checked_bl=1;
		        }
		    else{
                dialogBlood.dialog( "open" );

		    }

		});


		//Lung

		var checked_lg=0;
		$('#lung').click(function() {
		    if(checked_lg==0){
                //Now just reference this button and change CSS
                $(this).css('background-color','#16A085');
                $(this).data('clicked', true);
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                canvas.style.display="block";
                lung();
                }
                 dialogLung.dialog( "open" );
                checked_lg=1;
            }
            else{
                dialogLung.dialog( "open" );
            }
		});

	if (ModelForm.default) {
        var checked_h=0;
        var checked_g=0;
        var checked_p=0;
        var checked_m=0;
        var checked_sp=0;
	} else {
		// Heart
        var checked_h=0;
        $("#heart").click(function(e) {

            if(checked_h==0){
                    //Now just reference this button and change CSS
                    $(this).css('background-color','#16A085');
                    $(this).data('clicked', true);
                    if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                        canvas.style.display="block";
                        organ_dart($( "#heart" ));
                    }
                    dialogHeart.dialog( "open" );
                    checked_h=1;
            }
            else {

                    if (ModelForm.default) {
                        dialogHeart.dialog( "open" );
                    } else {
                        $("#dialog-confirm").html("Edit or Delete Heart?");

                        // Define the Dialog and its properties.
                        $("#dialog-confirm").dialog({
                            resizable: false,
                            modal: true,
                            title: "Heart",
                            height: 250,
                            width: 400,
                            buttons: {
                                "Delete": function () {
                                    $(this).dialog('close');
                                    delete_organ('heart');
                                    //delete residual from model replacing its parameters with 0.0
                                    $('#id_mod-heart_flow_factor').val("0.0");
                                    $('#id_mod-heart_volume_fraction').val("0.0");
                                    $('#id_mod-blood_heart_fraction').val("0.0");
                                    $('#id_dr-p_heart').val("0.0");
                                    $('#id_dr-pi_heart').val("0.0");
                                    checked_h=0;
                                    //callback(true);
                                },
                                "Cancel": function () {
                                        $(this).dialog('close');
                                        checked_h=1;
                                },
                                "Edit": function () {
                                        $(this).dialog('close');
                                        dialogHeart.dialog( "open" );
                                }
                            }
                        });
                    }

            }
        });

        // Muscle
        var checked_m=0;
        $("#muscle").click(function(e) {

            if(checked_m==0){
                    //Now just reference this button and change CSS
                    $(this).css('background-color','#16A085');
                    $(this).data('clicked', true);
                    if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                        canvas.style.display="block";
                        organ_dart($( "#muscle" ));
                    }
                    dialogMuscle.dialog( "open" );
                    checked_m=1;
            }
            else{

                    if (ModelForm.default) {
                        dialogMuscle.dialog( "open" );
                    } else {
                    $("#dialog-confirm").html("Edit or Delete Muscle?");

                    // Define the Dialog and its properties.
                    $("#dialog-confirm").dialog({
                        resizable: false,
                        modal: true,
                        title: "Muscle",
                        height: 250,
                        width: 400,
                        buttons: {
                            "Delete": function () {
                                $(this).dialog('close');
                                delete_organ('muscle');
                                //delete residual from model replacing its parameters with 0.0
                                $('#id_mod-muscle_flow_factor').val("0.0");
                                $('#id_mod-muscle_volume_fraction').val("0.0");
                                $('#id_mod-blood_muscle_fraction').val("0.0");
                                $('#id_dr-p_muscle').val("0.0");
                                $('#id_dr-pi_muscle').val("0.0");
                                checked_m=0;

                            },
                            "Cancel": function () {
                                    $(this).dialog('close');
                                    checked_m=1;
                            },
                            "Edit": function () {
                                    $(this).dialog('close');
                                    dialogMuscle.dialog( "open" );
                            }
                        }
                    });


                }
            }
        });

        // Spleen
        var checked_sp=0;
        $("#spleen").click(function(e) {

            if(checked_sp==0){
                    //Now just reference this button and change CSS
                    $(this).css('background-color','#16A085');
                    $(this).data('clicked', true);
                    if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                        canvas.style.display="block";
                        organ_dart($( "#spleen" ));
                    }
                    dialogSpleen.dialog( "open" );
                    checked_sp=1;
            }
            else{

                $("#dialog-confirm").html("Edit or Delete Spleen?");

                // Define the Dialog and its properties.
                $("#dialog-confirm").dialog({
                    resizable: false,
                    modal: true,
                    title: "Spleen",
                    height: 250,
                    width: 400,
                    buttons: {
                        "Delete": function () {
                            $(this).dialog('close');
                            delete_organ('spleen');
                            //delete residual from model replacing its parameters with 0.0
                            $('#id_mod-spleen_flow_factor').val("0.0");
                            $('#id_mod-spleen_volume_fraction').val("0.0");
                            $('#id_mod-blood_spleen_fraction').val("0.0");
                            $('#id_dr-p_spleen').val("0.0");
                            $('#id_dr-pi_spleen').val("0.0");
                            checked_sp=0;
                            //callback(true);
                        },
                        "Cancel": function () {
                                $(this).dialog('close');
                                checked_sp=1;
                        },
                        "Edit": function () {
                                $(this).dialog('close');
                                dialogSpleen.dialog( "open" );
                        }
                    }
                });
            }

        });

        // Placental
        var checked_p=0;
        $("#placental").click(function(e) {

        if(checked_p==0){
                //Now just reference this button and change CSS
                $(this).css('background-color','#16A085');
                $(this).data('clicked', true);
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    canvas.style.display="block";
                    organ_dart($( "#placental" ));
                }
                dialogPlacental.dialog( "open" );
                checked_p=1;
            }
            else {
                $("#dialog-confirm").html("Edit or Delete Placental?");

                // Define the Dialog and its properties.
                $("#dialog-confirm").dialog({
                    resizable: false,
                    modal: true,
                    title: "Placental",
                    height: 250,
                    width: 400,
                    buttons: {
                        "Delete": function () {
                            $(this).dialog('close');
                            delete_organ('placental');
                            //delete residual from model replacing its parameters with 0.0
                            $('#id_mod-placental_flow_factor').val("0.0");
                            $('#id_mod-placental_volume_fraction').val("0.0");
                            $('#id_mod-blood_placental_fraction').val("0.0");
                            $('#id_dr-p_placental').val("0.0");
                            $('#id_dr-pi_placental').val("0.0");
                            checked_p=0;
                        },
                        "Cancel": function () {
                                $(this).dialog('close');
                                checked_p=1;
                        },
                        "Edit": function () {
                                $(this).dialog('close');
                                dialogPlacental.dialog( "open" );
                        }
                    }
                });

            }
        });
    }

		function add_blood(organ) {
     	    $('#'+organ).css('background-color','#16A085');
    		//$("#Blood2").css('background-color','#16A085');
    		$('#'+organ).data('clicked', true);
    		if($('#residual').data('clicked') ){
    		    canvas.style.display="block";
    		    organ_dart($( "#residual" ));
    		}
    		if($('#skin').data('clicked') ){
    		    canvas.style.display="block";
    		    organ_dart($( "#skin" ));;
    		}
    		if($('#kidney').data('clicked') ){
    		    canvas.style.display="block";
    		    organ_dart($( "#kidney" ));
    		}
    		if($('#bladder').data('clicked') ){
    		    canvas.style.display="block";
    		    organ_dart($( "#bladder" ));
    		}
    		if($('#liver').data('clicked') ){
    		    canvas.style.display="block";
    		    liver();
    		}
    		if($('#lung').data('clicked') ){
    		    canvas.style.display="block";
    		    lung();
    		}
    		if($('#organ1').data('clicked')  ){
                 canvas.style.display="block";
                 neworgan($("#div-placental").position().left,$("#div-placental").position().top);
            }
            if($('#organ2').data('clicked')  ){
                 canvas.style.display="block";
                 neworgan($("#div-placental").position().left,$("#div-placental").position().top+50);
            }
            if($('#organ3').data('clicked')  ){
                 canvas.style.display="block";
                 neworgan($("#div-placental").position().left,$("#div-placental").position().top+100);
            }
            if($('#organ4').data('clicked')  ){
                 canvas.style.display="block";
                 neworgan($("#div-placental").position().left,$("#div-placental").position().top+150);
            }
            if($('#organ5').data('clicked')  ){
                 canvas.style.display="block";
                 neworgan($("#div-placental").position().left,$("#div-placental").position().top+200);
            }
            if($('#heart').data('clicked') ){
    		    canvas.style.display="block";
                organ_dart($( "#heart" ));
    		}
    		if($('#muscle').data('clicked') ){
    		    canvas.style.display="block";
                organ_dart($( "#muscle" ));
    		}
    		if($('#spleen').data('clicked') ){
    		    canvas.style.display="block";
                organ_dart($( "#spleen" ));
    		}
    		if($('#placental').data('clicked') ){
    		    canvas.style.display="block";
                organ_dart($( "#placental" ));
    		}

     	}

		function delete_organ(organ){

		    //Now just reference this button and change CSS
    		$('#'+organ).css('background-color','#D2D7D3');

            // Store the current transformation matrix
            ctx1.save();

            // Use the identity matrix while clearing the canvas
            ctx1.setTransform(1, 0, 0, 1, 0, 0);
            ctx1.clearRect(0, 0, canvas.width, canvas.height);

            ctx1.beginPath();

            // Restore the transform
            ctx1.restore();

            $('#'+organ).data('clicked', false);

            if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){

                if($('#skin').data('clicked') ){
                    //canvas.style.display="block";
                    organ_dart($( "#skin" ));;
                }
                if($('#residual').data('clicked') ){
                    //canvas.style.display="block";
                    organ_dart($( "#residual" ));
                }
                if($('#bladder').data('clicked') ){
                    //canvas.style.display="block";
                    organ_dart($( "#bladder" ));
                }
                if($('#liver').data('clicked') ){
                    //canvas.style.display="block";
                    liver();
                }
                if($('#lung').data('clicked') ){
                    //canvas.style.display="block";
                    lung();
                }
                if($('#kidney').data('clicked') ){
                    //canvas.style.display="block";
                    organ_dart($( "#kidney" ));
                }

                if($('#organ1').data('clicked') ){
                    canvas.style.display="block";
                    neworgan($("#div-placental").position().left,$("#div-placental").position().top);
                    }

                if($('#organ2').data('clicked') ){
                    canvas.style.display="block";
                    neworgan($("#div-placental").position().left,$("#div-placental").position().top+50);
                    }

                if($('#organ3').data('clicked') ){
                    canvas.style.display="block";
                    neworgan($("#div-placental").position().left,$("#div-placental").position().top+100);
                    }
                if($('#organ4').data('clicked') ){
                    canvas.style.display="block";
                    neworgan($("#div-placental").position().left,$("#div-placental").position().top+150);
                    }
                if($('#organ5').data('clicked') ){
                    canvas.style.display="block";
                    neworgan($("#div-placental").position().left,$("#div-placental").position().top+200);
                    }
                if($('#heart').data('clicked') ){
                    organ_dart($( "#heart" ));
                }
                if($('#muscle').data('clicked') ){
                    organ_dart($( "#muscle" ));
                }
                if($('#spleen').data('clicked') ){
                    organ_dart($( "#spleen" ));
                }
                if($('#placental').data('clicked') ){
                    organ_dart($( "#placental" ));
                }

            }

            if($('#skin').data('clicked') ){
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    //canvas.style.display="block";
                    organ_dart($( "#skin" ));
                    }
                }
            if($('#residual').data('clicked') ){
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    //canvas.style.display="block";
                    organ_dart($( "#residual" ));
                    }
                }
            if($('#bladder').data('clicked') ){
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    //canvas.style.display="block";
                    organ_dart($( "#bladder" ));
                    }
                }
            if($('#liver').data('clicked') ){
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    //canvas.style.display="block";
                    liver();
                    }
                }
            if($('#lung').data('clicked') ){
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    //canvas.style.display="block";
                    lung();
                    }
                }

            if($('#kidney').data('clicked') ){
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    //canvas.style.display="block";
                    organ_dart($( "#kidney" ));
                    }
                }
            if($('#organ1').data('clicked') ){

                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    canvas.style.display="block";
                    neworgan($("#div-placental").position().left,$("#div-placental").position().top);
                    }
             }

            if($('#organ2').data('clicked') ){

                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    canvas.style.display="block";
                    neworgan($("#div-placental").position().left,$("#div-placental").position().top+50);
                    }
             }

            if($('#organ3').data('clicked') ){

                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    canvas.style.display="block";
                    neworgan($("#div-placental").position().left,$("#div-placental").position().top+100);
                    }
             }

            if($('#organ4').data('clicked') ){

                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    canvas.style.display="block";
                    neworgan($("#div-placental").position().left,$("#div-placental").position().top+150);
                    }
             }

            if($('#organ5').data('clicked') ){

                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    canvas.style.display="block";
                    neworgan($("#div-placental").position().left,$("#div-placental").position().top+200);
                    }
             }
            if($('#heart').data('clicked') ){
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    organ_dart($( "#heart" ));
                    }
                }
            if($('#muscle').data('clicked') ){
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    organ_dart($( "#muscle" ));
                    }
                }
            if($('#spleen').data('clicked') ){
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    organ_dart($( "#spleen" ));
                    }
                }
            if($('#placental').data('clicked') ){
                if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    organ_dart($( "#placental" ));
                    }
                }

		}

		function delete_blood(organ){

		    //Now just reference this button and change CSS
    		$('#'+organ).css('background-color','#D2D7D3');

            // Store the current transformation matrix
            ctx1.save();

            // Use the identity matrix while clearing the canvas
            ctx1.setTransform(1, 0, 0, 1, 0, 0);
            ctx1.clearRect(0, 0, canvas.width, canvas.height);

            ctx1.beginPath();

            // Restore the transform
            ctx1.restore();

            $('#'+organ).data('clicked', false);


		}


if (ModelForm.default || ModelForm.edit || ModelForm.save) {

        if($("#id_mod-blood_rest_fraction").val() != "0.0" || $("#id_dr-p_rest").val() != "0.0" || $("#id_dr-pi_rest").val() != "0.0") {
            $("#residual").css('background-color','#16A085');
            organ_dart($( "#residual" ));
            $('#residual').data('clicked','true');
            checked_res=1;

        }
        if($("#id_mod-skin_flow_factor").val() != "0.0" || $("#id_mod-skin_volume_fraction").val() != "0.0" || $("#id_mod-blood_skin_fraction").val() != "0.0" || $("#id_dr-p_skin").val() != "0.0" || $("#id_dr-pi_skin").val() != "0.0") {
            $("#skin").css('background-color','#16A085');
            organ_dart($( "#skin" ));
            $('#skin').data('clicked','true');
            checked_sk=1;
        }
        if($("#id_mod-kidney_flow_factor").val() != "0.0" || $("#id_mod-kidney_volume_fraction").val() != "0.0" || $("#id_mod-blood_kidney_fraction").val() != "0.0" || $("#id_dr-p_kidney").val() != "0.0" || $("#id_dr-pi_kidney").val() != "0.0" || $("#id_dr-k_kidney").val() != "0.0") {
            $("#kidney").css('background-color','#16A085');
            organ_dart($( "#kidney" ));
            $('#kidney').data('clicked','true');
            checked_k=1;
        }
        if($("#id_mod-bladder_flow_factor").val() != "0.0" || $("#id_mod-bladder_volume_fraction").val() != "0.0" || $("#id_mod-blood_bladder_fraction").val() != "0.0" || $("#id_dr-p_bladder").val() != "0.0" || $("#id_dr-pi_bladder").val() != "0.0") {
            $("#bladder").css('background-color','#16A085');
            organ_dart($( "#bladder" ));
            $('#bladder').data('clicked','true');
            checked_bla=1;
        }
        if($("#id_mod-liver_flow_factor").val() != "0.0" || $("#id_mod-liver_volume_fraction").val() != "0.0" || $("#id_mod-blood_liver_fraction").val() != "0.0" || $("#id_dr-p_liver").val() != "0.0" || $("#id_dr-pi_liver").val() != "0.0" || $("#id_dr-k_met").val() != "0.0" || $("#id_dr-k_bile").val() != "0.0") {
            $("#liver").css('background-color','#16A085');
            liver();
            $('#liver').data('clicked','true');
            checked_liv=1;
        }
        if($("#id_mod-blood_volume_fraction").val() != "0.0" || $("#id_dr-pi_rbc").val() != "0.0" || $("#id_dr-pi_plasma").val() != "0.0") {
            $("#blood").css('background-color','#16A085');
            $("#Blood2").css('background-color','#16A085');
            canvas.style.display="block";
            $('#blood').data('clicked','true');
            $('#Blood2').data('clicked','true');
            checked_bl=1;
            checked_bl2=1;
        }
        if($("#id_mod-lung_flow_factor").val() != "0.0" || $("#id_mod-lung_volume_fraction").val() != "0.0" || $("#id_mod-blood_lung_fraction").val() != "0.0" || $("#id_dr-p_lung").val() != "0.0" || $("#id_dr-pi_lung").val() != "0.0") {
            $("#lung").css('background-color','#16A085');
            lung();
            $('#lung').data('clicked','true');
            checked_lg=1;
        }
         if($("#id_mod-heart_flow_factor").val() != "0.0" || $("#id_mod-heart_volume_fraction").val() != "0.0" || $("#id_mod-blood_heart_fraction").val() != "0.0" || $("#id_dr-p_heart").val() != "0.0" || $("#id_dr-pi_heart").val() != "0.0") {
            $("#heart").css('background-color','#16A085');
            organ_dart($( "#heart" ));
            $('#heart').data('clicked','true');
            checked_h=1;
        }
         if($("#id_mod-muscle_flow_factor").val() != "0.0" || $("#id_mod-muscle_volume_fraction").val() != "0.0" || $("#id_mod-blood_muscle_fraction").val() != "0.0" || $("#id_dr-p_muscle").val() != "0.0" || $("#id_dr-pi_muscle").val() != "0.0") {
            $("#muscle").css('background-color','#16A085');
            organ_dart($( "#muscle" ));
            $('#muscle').data('clicked','true');
            checked_m=1;
        }
         if($("#id_mod-spleen_flow_factor").val() != "0.0" || $("#id_mod-spleen_volume_fraction").val() != "0.0" || $("#id_mod-blood_spleen_fraction").val() != "0.0" || $("#id_dr-p_spleen").val() != "0.0" || $("#id_dr-pi_spleen").val() != "0.0") {
            $("#spleen").css('background-color','#16A085');
            organ_dart($( "#spleen" ));
            $('#spleen').data('clicked','true');
            checked_sp=1;
        }
         if($("#id_mod-placental_flow_factor").val() != "0.0" || $("#id_mod-placental_volume_fraction").val() != "0.0" || $("#id_mod-blood_placental_fraction").val() != "0.0" || $("#id_dr-p_placental").val() != "0.0" || $("#id_dr-pi_placental").val() != "0.0") {
            $("#placental").css('background-color','#16A085');
            organ_dart($( "#placental" ));
            $('#placental').data('clicked','true');
            checked_p=1;
        }
}

    //This function is called if user click an organ. If this organ is included to the model, displays a pop up window which ask user if he want edit or delete the clicked organ.
//Else user insert the organ parameters and the organ added to the model.

            function organ_click(){

                //organ1 click

                $('#organ1').click(function() {

                    if(!$('#organ1').data('clicked')){
                        //Now just reference this button and change CSS
                        $("#organ1").css('background-color','#16A085');
                        $("#organ1").data('clicked', true);
                        if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                        canvas.style.display="block";
                        neworgan($("#div-placental").position().left,$("#div-placental").position().top);
                        }
                        //dialogLiver.dialog( "open" );
                        dialogOrgan1.dialog( "open" );


                    }
                    else{
                        $("#dialog-confirm").html("Edit or Delete?");

                        // Define the Dialog and its properties.
                        $("#dialog-confirm").dialog({
                            resizable: false,
                            modal: true,
                            title: "Delete ",
                            height: 250,
                            width: 400,
                            buttons: {
                                "Delete": function () {
                                    $("#dialog-confirm").dialog('close');
                                    delete_organ('organ1');
                                    $('#id_mod-organ1_flow_factor').val("0.0");
                                    $('#id_mod-organ1_volume_fraction').val("0.0");
                                    $('#id_mod-blood_organ1_fraction').val("0.0");
                                    $('#id_dr-p_organ1').val("0.0");
                                    $('#id_dr-pi_organ1').val("0.0");
                                    $("#org1_f_f").val("0.0");
                                    $("#org1_v_f").val("0.0");
                                    $("#org1_b_f").val("0.0");
                                    $('#p_org1').val("0.0");
                                    $('#pi_org1').val("0.0");
                                    var org = JSON.parse( $("#id_dr-organ1_params").val() );
                                    org[0]= {type: NULL}
                                    $("#id_dr-organ1_params").val( JSON.stringify(org) );
                                    $("#non-metabolise1").attr("checked", false);
                                    $("#metabolise1").attr("checked", false);
                                    $("#meta-const1").hide()

                                    //callback(true);
                                },
                                "Cancel": function () {
                                        $("#dialog-confirm").dialog('close');
                                        //dialogSkin.dialog( "open" );
                                        //callback(false);

                                },
                                "Edit": function () {
                                $(this).dialog('close');
                                dialogOrgan1.dialog( "open" );
                                }
                            }
                        });

                    }
                });

                //organ2 click

                $('#organ2').click(function() {

                    if(!$('#organ2').data('clicked')){
                    //Now just reference this button and change CSS
                    $(this).css('background-color','#16A085');
                    $(this).data('clicked', true);
                    if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    canvas.style.display="block";
                    neworgan($("#div-placental").position().left,$("#div-placental").position().top+50);
                    }
                    //dialogLiver.dialog( "open" );
                    dialogOrgan2.dialog( "open" );

                    }
                    else{
                        $("#dialog-confirm").html("Edit or Delete?");

                        // Define the Dialog and its properties.
                        $("#dialog-confirm").dialog({
                            resizable: false,
                            modal: true,
                            title: "Delete",
                            height: 250,
                            width: 400,
                            buttons: {
                                "Delete": function () {
                                    $(this).dialog('close');
                                    delete_organ('organ2');
                                    $('#id_mod-organ2_flow_factor').val("0.0");
                                    $('#id_mod-organ2_volume_fraction').val("0.0");
                                    $('#id_mod-blood_organ2_fraction').val("0.0");
                                    $('#id_dr-p_organ2').val("0.0");
                                    $('#id_dr-pi_organ2').val("0.0");
                                    $("#org2_f_f").val("0.0");
                                    $("#org2_v_f").val("0.0");
                                    $("#org2_b_f").val("0.0");
                                    $('#p_org2').val("0.0");
                                    $('#pi_org2').val("0.0");
                                    var org = JSON.parse( $("#id_dr-organ2_params").val() );
                                    org[1]= {type: NULL};
                                    $("#id_dr-organ1_params").val( JSON.stringify(org) );
                                    $("#non-metabolise2").attr("checked", false);
                                    $("#metabolise2").attr("checked", false);
                                    $("#meta-const2").hide()

                                    //callback(true);
                                },
                                "Cancel": function () {
                                        $(this).dialog('close');
                                        //dialogSkin.dialog( "open" );
                                        //callback(false);

                                },
                                 "Edit": function () {
                                        $(this).dialog('close');
                                        dialogOrgan2.dialog( "open" );
                                }
                            }
                        });

                    }

                });

                //organ3 click

                $('#organ3').click(function() {

                    if(!$('#organ3').data('clicked')){
                    //Now just reference this button and change CSS
                    $(this).css('background-color','#16A085');
                    $(this).data('clicked', true);
                    if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    canvas.style.display="block";
                    neworgan($("#div-placental").position().left,$("#div-placental").position().top+100);
                    }
                    //dialogLiver.dialog( "open" );
                    dialogOrgan3.dialog( "open" );

                    }
                    else{
                        $("#dialog-confirm").html("Edit or Delete?");

                        // Define the Dialog and its properties.
                        $("#dialog-confirm").dialog({
                            resizable: false,
                            modal: true,
                            title: "Delete",
                            height: 250,
                            width: 400,
                            buttons: {
                                "Delete": function () {
                                    $(this).dialog('close');
                                    delete_organ('organ3');
                                    $('#id_mod-organ3_flow_factor').val("0.0");
                                    $('#id_mod-organ3_volume_fraction').val("0.0");
                                    $('#id_mod-blood_organ3_fraction').val("0.0");
                                    $('#id_dr-p_organ3').val("0.0");
                                    $('#id_dr-pi_organ3').val("0.0");
                                    $("#org3_f_f").val("0.0");
                                    $("#org3_v_f").val("0.0");
                                    $("#org3_b_f").val("0.0");
                                    $('#p_org3').val("0.0");
                                    $('#pi_org3').val("0.0");
                                    var org = JSON.parse( $("#id_dr-organ1_params").val() );
                                    org[2]= {type: NULL};
                                    $("#id_dr-organ1_params").val( JSON.stringify(org) );
                                    $("#non-metabolise3").attr("checked", false);
                                    $("#metabolise3").attr("checked", false);
                                    $("#meta-const3").hide()

                                    //callback(true);
                                },
                                "Cancel": function () {
                                        $(this).dialog('close');
                                        //dialogSkin.dialog( "open" );
                                        //callback(false);

                                },
                                "Edit": function () {
                                        $(this).dialog('close');
                                        dialogOrgan3.dialog( "open" );
                                }
                            }
                        });

                    }

                });


                //organ4 click

                $('#organ4').click(function() {

                    if(!$('#organ4').data('clicked')){
                    //Now just reference this button and change CSS
                    $(this).css('background-color','#16A085');
                    $(this).data('clicked', true);
                    if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    canvas.style.display="block";
                    neworgan($("#div-placental").position().left,$("#div-placental").position().top+150);
                    }
                    //dialogLiver.dialog( "open" );
                    dialogOrgan4.dialog( "open" );

                    }
                    else{
                        $("#dialog-confirm").html("Edit or Delete?");

                        // Define the Dialog and its properties.
                        $("#dialog-confirm").dialog({
                            resizable: false,
                            modal: true,
                            title: "Delete",
                            height: 250,
                            width: 400,
                            buttons: {
                                "Delete": function () {
                                    $(this).dialog('close');
                                    delete_organ('organ4');
                                    $('#id_mod-organ4_flow_factor').val("0.0");
                                    $('#id_mod-organ4_volume_fraction').val("0.0");
                                    $('#id_mod-blood_organ4_fraction').val("0.0");
                                    $('#id_dr-p_organ4').val("0.0");
                                    $('#id_dr-pi_organ4').val("0.0");
                                    $("#org4_f_f").val("0.0");
                                    $("#org4_v_f").val("0.0");
                                    $("#org4_b_f").val("0.0");
                                    $('#p_org4').val("0.0");
                                    $('#pi_org4').val("0.0");
                                    var org = JSON.parse( $("#id_dr-organ1_params").val() );
                                    org[3]= {type: NULL};
                                    $("#id_dr-organ1_params").val( JSON.stringify(org) );
                                    $("#non-metabolise4").attr("checked", false);
                                    $("#metabolise4").attr("checked", false);
                                    $("#meta-const4").hide()

                                    //callback(true);
                                },
                                "Cancel": function () {
                                        $(this).dialog('close');
                                        //dialogSkin.dialog( "open" );
                                        //callback(false);

                                },
                                "Edit": function () {
                                        $(this).dialog('close');
                                        dialogOrgan4.dialog( "open" );
                                }
                            }
                        });

                    }

                });


                //organ5 click

                $('#organ5').click(function() {

                    if(!$('#organ5').data('clicked')){
                    //Now just reference this button and change CSS
                    $(this).css('background-color','#16A085');
                    $(this).data('clicked', true);
                    if($('#blood').data('clicked') || $('#Blood2').data('clicked') ){
                    canvas.style.display="block";
                    neworgan($("#div-placental").position().left,$("#div-placental").position().top+200);
                    }
                    //dialogLiver.dialog( "open" );
                    dialogOrgan5.dialog( "open" );

                    }
                    else{
                        $("#dialog-confirm").html("Edit or Delete?");

                        // Define the Dialog and its properties.
                        $("#dialog-confirm").dialog({
                            resizable: false,
                            modal: true,
                            title: "Delete",
                            height: 250,
                            width: 400,
                            buttons: {
                                "Delete": function () {
                                    $(this).dialog('close');
                                    delete_organ('organ5');
                                    $('#id_mod-organ5_flow_factor').val("0.0");
                                    $('#id_mod-organ5_volume_fraction').val("0.0");
                                    $('#id_mod-blood_organ2_fraction').val("0.0");
                                    $('#id_dr-p_organ5').val("0.0");
                                    $('#id_dr-pi_organ5').val("0.0");
                                    $("#org5_f_f").val("0.0");
                                    $("#org5_v_f").val("0.0");
                                    $("#org5_b_f").val("0.0");
                                    $('#p_org5').val("0.0");
                                    $('#pi_org5').val("0.0");
                                    var org = JSON.parse( $("#id_dr-organ1_params").val() );
                                    org[4]= {type: NULL};
                                    $("#id_dr-organ1_params").val( JSON.stringify(org) );
                                    $("#non-metabolise5").attr("checked", false);
                                    $("#metabolise5").attr("checked", false);
                                    $("#meta-const5").hide()

                                    //callback(true);
                                },
                                "Cancel": function () {
                                        $(this).dialog('close');
                                        //dialogSkin.dialog( "open" );
                                        //callback(false);

                                },
                                "Edit": function () {
                                        $(this).dialog('close');
                                        dialogOrgan5.dialog( "open" );
                                }
                            }
                        });

                    }

                });

            }
             organ_click();


        //Display additional organs
        //counter is the number of added organs that included in the model.
        if ($('#counter_id').val() > 1){
	    for (i = 2; i <= $('#counter_id').val(); i++) {
            //$('input[name= "Add_organs"]').click();
            if(i==2){
            $("#id_mod-organ1_flow_factor").val( $("#org1_f_fc").val() );
            $("#id_mod-organ1_volume_fraction").val( $("#org1_v_fc").val() );
            $("#id_mod-blood_organ1_fraction").val( $("#org1_b_fc").val() );

            $("#organ1").val($("#id_mod-organ1_name").val() );
            document.getElementById('organ1').style.display = 'block';
             if($("#id_mod-organ1_flow_factor").val() != "0.0" || $("#id_mod-organ1_volume_fraction").val() != "0.0" || $("#id_mod-blood_organ1_fraction").val() != "0.0" || $("#id_dr-p_organ1").val() != "0.0" || $("#id_dr-pi_organ1").val() != "0.0"){
                $('#organ1').css('background-color','#16A085');
                $('#organ1').data('clicked', true);

                }
                counter++;


            $('#blood').animate({height: '+=80'}, 500);
            $('#Blood2').animate({height: '+=80'}, 500);
            $('#Create_model').animate({top: '+=50'}, 500);
            $('#Add_organs').animate({top: '+=50'}, 500);
            $('#removeButton').animate({top: '+=50'}, 500);


            if(($('#blood').data('clicked') || $('#Blood2').data('clicked')) && ($('#organ1').data('clicked')) ){
                canvas.style.display="block";
                neworgan($("#div-placental").position().left,$("#div-placental").position().top);
            }

            $("#org1").val($("#id_mod-organ1_name").val() );
            $("#org1_f_f").val( $("#id_mod-organ1_flow_factor").val() );
            $("#org1_v_f").val( $("#id_mod-organ1_volume_fraction").val() );
            $("#org1_b_f").val( $("#id_mod-blood_organ1_fraction").val() );


            }
            if(i==3){
            $("#id_mod-organ2_flow_factor").val( $("#org2_f_fc").val() );
            $("#id_mod-organ2_volume_fraction").val( $("#org2_v_fc").val() );
            $("#id_mod-blood_organ2_fraction").val( $("#org2_b_fc").val() );

            $("#organ2").val($("#id_mod-organ2_name").val() );
            document.getElementById('organ2').style.display = 'block';
            if($("#id_mod-organ2_flow_factor").val() != "0.0" || $("#id_mod-organ2_volume_fraction").val() != "0.0" || $("#id_mod-blood_organ2_fraction").val() != "0.0" || $("#id_dr-p_organ2").val() != "0.0" || $("#id_dr-pi_organ2").val() != "0.0"){
                $('#organ2').css('background-color','#16A085');
                $('#organ2').data('clicked', true);
            }
            counter++;

            $('#blood').animate({height: '+=50'}, 500);
            $('#Blood2').animate({height: '+=50'}, 500);
            $('#Create_model').animate({top: '+=50'}, 500);
            $('#Add_organs').animate({top: '+=50'}, 500);
            $('#removeButton').animate({top: '+=50'}, 500);


            if(($('#blood').data('clicked') || $('#Blood2').data('clicked')) && ($('#organ2').data('clicked')) ){
                canvas.style.display="block";
                neworgan($("#div-placental").position().left,$("#div-placental").position().top + 50);
            }

            $("#org2").val($("#id_mod-organ2_name").val() );
            $("#org2_f_f").val( $("#id_mod-organ2_flow_factor").val() );
            $("#org2_v_f").val( $("#id_mod-organ2_volume_fraction").val() );
            $("#org2_b_f").val( $("#id_mod-blood_organ2_fraction").val() );
            }
            if(i==4){
            $("#id_mod-organ3_flow_factor").val( $("#org3_f_fc").val() );
            $("#id_mod-organ3_volume_fraction").val( $("#org3_v_fc").val() );
            $("#id_mod-blood_organ3_fraction").val( $("#org3_b_fc").val() );

            $("#organ3").val($("#id_mod-organ3_name").val() );
            document.getElementById('organ3').style.display = 'block';
            if($("#id_mod-organ3_flow_factor").val() != "0.0" || $("#id_mod-organ3_volume_fraction").val() != "0.0" || $("#id_mod-blood_organ3_fraction").val() != "0.0" || $("#id_dr-p_organ3").val() != "0.0" || $("#id_dr-pi_organ3").val() != "0.0"){
                $('#organ3').css('background-color','#16A085');
                $('#organ3').data('clicked', true);
            }
            counter++;

            $('#blood').animate({height: '+=50'}, 500);
            $('#Blood2').animate({height: '+=50'}, 500);
            $('#Create_model').animate({top: '+=50'}, 500);
            $('#Add_organs').animate({top: '+=50'}, 500);
            $('#removeButton').animate({top: '+=50'}, 500);


            if(($('#blood').data('clicked') || $('#Blood2').data('clicked')) && ($('#organ3').data('clicked')) ){
                canvas.style.display="block";
                neworgan($("#div-placental").position().left,$("#div-placental").position().top + 100);
            }

            $("#org3").val($("#id_mod-organ3_name").val() );
            $("#org3_f_f").val( $("#id_mod-organ3_flow_factor").val() );
            $("#org3_v_f").val( $("#id_mod-organ3_volume_fraction").val() );
            $("#org3_b_f").val( $("#id_mod-blood_organ3_fraction").val() );
            }
            if(i==5){
            $("#id_mod-organ4_flow_factor").val( $("#org4_f_fc").val() );
            $("#id_mod-organ4_volume_fraction").val( $("#org4_v_fc").val() );
            $("#id_mod-blood_organ4_fraction").val( $("#org4_b_fc").val() );

            $("#orga4").val($("#id_mod-organ4_name").val() );
            document.getElementById('organ4').style.display = 'block';
            if($("#id_mod-organ4_flow_factor").val() != "0.0" || $("#id_mod-organ4_volume_fraction").val() != "0.0" || $("#id_mod-blood_organ4_fraction").val() != "0.0" || $("#id_dr-p_organ4").val() != "0.0" || $("#id_dr-pi_organ4").val() != "0.0"){
                $('#organ4').css('background-color','#16A085');
                $('#organ4').data('clicked', true);
                }
            counter++;

            $('#blood').animate({height: '+=50'}, 500);
            $('#Blood2').animate({height: '+=50'}, 500);
            $('#Create_model').animate({top: '+=50'}, 500);
            $('#Add_organs').animate({top: '+=50'}, 500);
            $('#removeButton').animate({top: '+=50'}, 500);


            if(($('#blood').data('clicked') || $('#Blood2').data('clicked')) && ($('#organ4').data('clicked')) ){
                canvas.style.display="block";
                neworgan($("#div-placental").position().left,$("#div-placental").position().top + 150);
            }

            $("#org4").val($("#id_mod-organ4_name").val() );
            $("#org4_f_f").val( $("#id_mod-organ4_flow_factor").val() );
            $("#org4_v_f").val( $("#id_mod-organ4_volume_fraction").val() );
            $("#org4_b_f").val( $("#id_mod-blood_organ4_fraction").val() );
            }
            if(i==6){
            $("#id_mod-organ5_flow_factor").val( $("#org5_f_fc").val() );
            $("#id_mod-organ5_volume_fraction").val( $("#org5_v_fc").val() );
            $("#id_mod-blood_organ5_fraction").val( $("#org5_b_fc").val() );

            $("#organ5").val($("#id_mod-organ5_name").val() );
            document.getElementById('organ5').style.display = 'block';
            if($("#id_mod-organ5_flow_factor").val() != "0.0" || $("#id_mod-organ5_volume_fraction").val() != "0.0" || $("#id_mod-blood_organ5_fraction").val() != "0.0" || $("#id_dr-p_organ5").val() != "0.0" || $("#id_dr-pi_organ5").val() != "0.0"){
                $('#organ5').css('background-color','#16A085');
                $('#organ5').data('clicked', true);
            }
            counter++;

            $('#blood').animate({height: '+=50'}, 500);
            $('#Blood2').animate({height: '+=50'}, 500);
            $('#Create_model').animate({top: '+=50'}, 500);
            $('#Add_organs').animate({top: '+=50'}, 500);
            $('#removeButton').animate({top: '+=50'}, 500);


            if(($('#blood').data('clicked') || $('#Blood2').data('clicked')) && ($('#organ5').data('clicked')) ){
                canvas.style.display="block";
                neworgan($("#div-placental").position().left,$("#div-placental").position().top + 200);
            }

            $("#org5").val($("#id_mod-organ5_name").val() );
            $("#org5_f_f").val( $("#id_mod-organ5_flow_factor").val() );
            $("#org5_v_f").val( $("#id_mod-organ5_volume_fraction").val() );
            $("#org5_b_f").val( $("#id_mod-blood_organ5_fraction").val() );
            }
        }
	}

//Remove the last organ which has been inserted
             $("#removeButton").click(function () {
                if(counter ==1){
                      alert("No more textbox to remove");
                      return false;
                   }

                counter--;
                $('#counter_id').val(+counter);
                document.getElementById('organ' + counter).style.display = 'none';
                $('#organ'+counter).data('clicked', false);

                $('#blood').animate({height: '-=50'}, 500);
                $('#Blood2').animate({height: '-=50'}, 500);
                $('#Create_model').animate({top: '-=50'}, 500);
                $('#Add_organs').animate({top: '-=50'}, 500);
                $('#removeButton').animate({top: '-=50'}, 500);

                // $("#organ" + counter).remove();
                delete_organ('organ'+ counter);
                $('#id_mod-organ'+ counter +'_name').val("");
                $('#id_mod-organ' + counter + '_flow_factor').val("0.0");
                $('#id_mod-organ' + counter + '_volume_fraction').val("0.0");
                $('#id_mod-blood_organ' + counter + '_fraction').val("0.0");
                $('#id_dr-p_organ' + counter).val("0.0");
                $('#id_dr-pi_organ' + counter).val("0.0");
                $('#org' + counter + '_f_fc').val("0.0");
                $('#org' + counter + '_v_fc').val("0.0");
                $('#org' + counter + '_b_fc').val("0.0");
                $('#p_org' + counter).val("0.0");
                $('#pi_org' + counter).val("0.0");
                $('#org' + counter + 'c').val("");
                $('#organ' + counter + 'name').val("");
                $('#organ' + counter + 'nam').val("");
                $('#organ' + counter).val("");
                $('#k_met' + counter).val("0.0");
                $('#k_bile' + counter).val("0.0");
                var org = JSON.parse( $("#id_dr-organ1_params").val() );
                org[counter-1]= null;
                $("#id_dr-organ1_params").val( JSON.stringify(org) );
                $("#non-metabolise" + counter).attr("checked", false);
                $("#metabolise" + counter).attr("checked", false);
                $("#meta-const" + counter).hide();

            });

//MPC -->

    $('#close-loop').removeClass('disabled');
    $('#open').removeClass('disabled');
    $('#mpc').removeClass('disabled');
    $('#pid').removeClass('disabled');
    $('#close-loop').addClass('enabled');
    $('#open').addClass('enabled');
    $('#mpc').addClass('enabled');
    $('#pid').addClass('enabled');

    $('a#mpc').click(function(){
		    //get the json object from the method_params field
		    var params_json = JSON.parse( $("#id_mod-method_params").val() );
            $("#Np").val(params_json.N);
            $("#step_p").val(params_json.step);
            $("#total_t").val(params_json.end);
            $("#inter").val(params_json.intervals);
            $("#q_weight").val(params_json.Q);
            $("#r_weight").val(params_json.R);
            $("#params-close").val(JSON.stringify(params_json));
            if ($("#total_t").val() != "" &&  $("#inter").val() != ""){
                $("#submit_close").click();
                }
            dialogSet.dialog( "open" );
        });

    $('a#open').click(function(){

            var params_json = JSON.parse( $("#id_mod-method_params").val() );
            $("#Time").val(params_json.total_time);
            $("#N_int").val(params_json.total_N);
            $("#params-open").val(JSON.stringify(params_json));
            dialogOpen.dialog( "open" );
            //if Time and N_int field have values click submit
            if ($("#Time").val() != "" &&  $("#N_int").val() != ""){
                $("#submit_open").click();
                }
            dialogOpen.dialog( "open" );



        })

//Define drug properties pop up -->

         $(function() {
            var buttons;
            if (ModelForm.default) {
                buttons = {"OK":{
				    text: "OK",
				    id: "drug-ok",
				    click: function() {
						dialogDrug.dialog( "close" );
					}
					}
                }
            } else {
                buttons = {
                    "Save changes":{
                    text: "Save changes",
					click: function() {
					    $("#id_dr-drug_name").val( $("#drugname").val() );
					    $("#id_dr-max_influx").val( $("#max_influx").val() );
					    $("#id_dr-p_rest").val( $("#p_rest").val() );
						$("#id_dr-pi_rest").val( $("#pi_rest").val() );
						$("#id_dr-max_residual").val( $("#max_rest").val() );
						$("#id_dr-min_residual").val( $("#min_rest").val() );
						$("#id_dr-p_skin").val( $("#p_sk").val() );
						$("#id_dr-pi_skin").val( $("#pi_sk").val() );
						$("#id_dr-max_skin").val( $("#max_sk").val() );
						$("#id_dr-min_skin").val( $("#min_sk").val() );
						$("#id_dr-p_kidney").val( $("#p_kid").val() );
						$("#id_dr-pi_kidney").val( $("#pi_kid").val() );
						$("#id_dr-k_kidney").val( $("#kin_kidney").val() );
						$("#id_dr-max_kidney").val( $("#max_kidney").val() );
						$("#id_dr-min_kidney").val( $("#min_kidney").val() );
						$("#id_dr-p_bladder").val( $("#p_bl").val() );
						$("#id_dr-pi_bladder").val( $("#pi_bl").val() );
						$("#id_dr-max_bladder").val( $("#max_bl").val() );
						$("#id_dr-min_bladder").val( $("#min_bl").val() );
						$("#id_dr-p_liver").val( $("#p_liv").val() );
						$("#id_dr-pi_liver").val( $("#pi_liv").val() );
						$("#id_dr-max_liver").val( $("#max_liv").val() );
						$("#id_dr-min_liver").val( $("#min_liv").val() );
						$("#id_dr-k_met").val( $("#kin_met").val() );
						$("#id_dr-k_bile").val( $("#kin_bile").val() );
						$("#id_dr-pi_rbc").val( $("#pi_rb").val() );
						$("#id_dr-pi_plasma").val( $("#pi_pl").val() );
						$("#id_dr-p_lung").val( $("#p_lg").val() );
						$("#id_dr-pi_lung").val( $("#pi_lg").val() );
						$("#id_dr-max_lung").val( $("#max_lg").val() );
						$("#id_dr-min_lung").val( $("#min_lg").val() );
						//organ1
						$("#id_dr-p_organ1").val( $("#p_org1").val() );
                        $("#id_dr-pi_organ1").val( $("#pi_org1").val() );
                        //Get the type of the organ
                        /*$("#organ1type").val( $('#dialog-drug').find('input:checked').val() );
                        //If type of organ is metabolising
                        if( $("#organ1type").val() == "met"){
                        //Get the selected option(constains) from pop up window
                            $('select[name="constains1" ]').val($('select[name="const"]').val() );

                            }*/
                        if( $('#t1').find('input:checked').val() == "met"){
                            var organ1_params_json= [{
                                type: $('#t1').find('input:checked').val(),
                                const: $('select[name="const"]').val(),
                                k_met: $("#k_met1").val(),
                                k_bile: $("#k_bile1").val()
                            }]
                        }
                        else if( $('#t1').find('input:checked').val() == "non-met"){
                            var organ1_params_json= [{
                                type: $('#t1').find('input:checked').val()
                            }]
                        }
                        else {
                            var organ1_params_json= [{
                                type: "NULL"
                            }]
                        }
                         //pass json to field to be read by the view
                        //$("#id_dr-organ1_params").val( JSON.stringify(organ1_params_json) );
                        //organ2
                         $("#id_dr-p_organ2").val( $("#p_org2").val() );
                         $("#id_dr-pi_organ2").val( $("#pi_org2").val() );
                         //Get the type of the organ
                         if( $('#t2').find('input:checked').val() == "met"){
                            var organ2_params_json= {
                                type: $('#t2').find('input:checked').val(),
                                const: $('select[name="const2"]').val(),
                                k_met: $("#k_met2").val(),
                                k_bile: $("#k_bile2").val()
                            }
                         }
                         else if( $('#t2').find('input:checked').val() == "non-met"){
                            var organ2_params_json= {
                                type: $('#t2').find('input:checked').val()
                            }
                         }
                         else {
                            var organ2_params_json= {
                                type: "NULL"
                            }
                        }
                         //pass json to field to be read by the view
                         if(organ1_params_json != null){
                         organ1_params_json.push(organ2_params_json);
                         }
                        $("#id_dr-organ1_params").val( JSON.stringify(organ1_params_json) );
                         //organ3
                         $("#id_dr-p_organ3").val( $("#p_org3").val() );
                         $("#id_dr-pi_organ3").val( $("#pi_org3").val() );

                         //Get the type of the organ
                         if( $('#t3').find('input:checked').val() == "met"){
                            var organ3_params_json= {
                                type: $('#t3').find('input:checked').val(),
                                const: $('select[name="const3"]').val(),
                                k_met: $("#k_met3").val(),
                                k_bile: $("#k_bile3").val()
                            }
                         }
                         else if( $('#t3').find('input:checked').val() == "non-met"){
                            var organ3_params_json= {
                                type: $('#t3').find('input:checked').val()
                            }
                         }
                         else {
                            var organ3_params_json= {
                                type: "NULL"
                            }
                         }
                         //pass json to field to be read by the view
                         if(organ1_params_json != null){
                            organ1_params_json.push(organ3_params_json);
                         }
                        $("#id_dr-organ1_params").val( JSON.stringify(organ1_params_json) );
                         //organ4
                         $("#id_dr-p_organ4").val( $("#p_org4").val() );
                         $("#id_dr-pi_organ4").val( $("#pi_org4").val() );
                         //Get the type of the organ
                         if( $('#t4').find('input:checked').val() == "met"){
                            var organ4_params_json= {
                                type: $('#t4').find('input:checked').val(),
                                const: $('select[name="const4"]').val(),
                                k_met: $("#k_met4").val(),
                                k_bile: $("#k_bile4").val()
                            }
                         }
                         else if( $('#t4').find('input:checked').val() == "non-met"){
                            var organ4_params_json= {
                                type: $('#t4').find('input:checked').val()
                            }
                         }
                         else {
                            var organ4_params_json= {
                                type: "NULL"
                            }
                         }
                         //pass json to field to be read by the view
                         if(organ1_params_json != null){
                             organ1_params_json.push(organ4_params_json);
                             }
                         $("#id_dr-organ1_params").val( JSON.stringify(organ1_params_json) );
                         //organ5
                         $("#id_dr-p_organ5").val( $("#p_org5").val() );
                         $("#id_dr-pi_organ5").val( $("#pi_org5").val() );
                         //Get the type of the organ
                         if( $('#t5').find('input:checked').val() == "met"){
                            var organ5_params_json= {
                                type: $('#t5').find('input:checked').val(),
                                const: $('select[name="const5"]').val(),
                                k_met: $("#k_met5").val(),
                                k_bile: $("#k_bile5").val()
                            }
                         }
                         else if( $('#t5').find('input:checked').val() == "non-met"){
                            var organ5_params_json= {
                                type: $('#t5').find('input:checked').val()
                            }
                         }
                         else {
                            var organ5_params_json= {
                                type: "NULL"
                            }
                         }
                         //pass json to field to be read by the view
                        if(organ1_params_json != null){
                            organ1_params_json.push(organ5_params_json);
                        }
                        $("#id_dr-organ1_params").val( JSON.stringify(organ1_params_json) );

                        $("#id_dr-p_heart").val( $("#p_h").val() );
						$("#id_dr-pi_heart").val( $("#pi_h").val() );
						$("#id_dr-max_heart").val( $("#max_h").val() );
						$("#id_dr-min_heart").val( $("#min_h").val() );
						$("#id_dr-p_muscle").val( $("#p_m").val() );
						$("#id_dr-pi_muscle").val( $("#pi_m").val() );
						$("#id_dr-max_muscle").val( $("#max_m").val() );
						$("#id_dr-min_muscle").val( $("#min_m").val() );
						$("#id_dr-p_spleen").val( $("#p_sp").val() );
						$("#id_dr-pi_spleen").val( $("#pi_sp").val() );
						$("#id_dr-max_spleen").val( $("#max_sp").val() );
						$("#id_dr-min_spleen").val( $("#min_sp").val() );
						$("#id_dr-p_placental").val( $("#p_p").val() );
						$("#id_dr-pi_placental").val( $("#pi_p").val() );
						$("#id_dr-max_placental").val( $("#max_p").val() );
						$("#id_dr-min_placental").val( $("#min_p").val() );

						/*$("#").val( $("#N_int").val() );*/
						dialogDrug.dialog( "close" );
					}
					}
                }
            }

			dialogDrug = $( "#dialog-drug" ).dialog({
				autoOpen: false,
				modal: true,
				width: 808,
				height: 520,
				left: 300,
				top: 200,
				buttons: buttons
			});

		});


        $('a#drug').click(function(){

        $("#organ1name").val(  $("#organ1").val() );
        $("#organ2name").val(  $("#organ2").val() );
        $("#organ3name").val(  $("#organ3").val() );
        $("#organ4name").val(  $("#organ4").val() );
        $("#organ5name").val(  $("#organ5").val() );
        $("#organ1nam").val(  $("#organ1").val() );
        $("#organ2nam").val(  $("#organ2").val() );
        $("#organ3nam").val(  $("#organ3").val() );
        $("#organ4nam").val(  $("#organ4").val() );
        $("#organ5nam").val(  $("#organ5").val() );

        //get the json object from the method_params field
        if($("#id_dr-organ1_params").val() != []){
            var organ1_params_json = JSON.parse( $("#id_dr-organ1_params").val() );
                if(organ1_params_json[0] != null){
                    if (organ1_params_json[0].type == "met"){
                        $('input:radio[name=type1][value="met"]').click();
                        if (organ1_params_json[0].const == "Linear"){
                            $("#const").val("Linear");
                            }
                        if (organ1_params_json[0].const == "Menten"){
                            $("#const").val("Menten");
                            }
                        $("#k_met1").val(organ1_params_json[0].k_met);
                        $("#k_bile1").val(organ1_params_json[0].k_bile);

                    }
                    if (organ1_params_json[0].type == "non-met"){
                        $('input:radio[name=type1][value="non-met"]').click();

                    }
                }
                if(organ1_params_json[1] != null){
                    if (organ1_params_json[1].type == "met"){
                        $('input:radio[name=type2][value="met"]').click();
                        if (organ1_params_json[1].const == "Linear"){
                            $("#const2").val("Linear");
                            }
                        if (organ1_params_json[1].const == "Menten"){
                            $("#const2").val("Menten");
                            }
                        $("#k_met2").val(organ1_params_json[1].k_met);
                        $("#k_bile2").val(organ1_params_json[1].k_bile);
                    }
                    if (organ1_params_json[1].type == "non-met"){
                        $('input:radio[name=type2][value="non-met"]').click();

                    }
                }
                if(organ1_params_json[2] != null){
                    if (organ1_params_json[2].type == "met"){
                        $('input:radio[name=type3][value="met"]').click();
                        if (organ1_params_json[2].const == "Linear"){
                            $("#const3").val("Linear");
                            }
                        if (organ1_params_json[2].const == "Menten"){
                            $("#const3").val("Menten");
                            }
                        $("#k_met3").val(organ1_params_json[2].k_met);
                        $("#k_bile3").val(organ1_params_json[2].k_bile);
                    }
                    if (organ1_params_json[2].type == "non-met"){
                        $('input:radio[name=type3][value="non-met"]').click();

                    }
                }
                if(organ1_params_json[3] != null){
                    if (organ1_params_json[3].type == "met"){
                        $('input:radio[name=type4][value="met"]').click();
                        if (organ1_params_json[3].const == "Linear"){
                            $("#const4").val("Linear");
                            }
                        if (organ1_params_json[3].const == "Menten"){
                            $("#const4").val("Menten");
                            }
                        $("#k_met4").val(organ1_params_json[3].k_met);
                        $("#k_bile4").val(organ1_params_json[3].k_bile);
                    }
                    if (organ1_params_json[3].type == "non-met"){
                        $('input:radio[name=type4][value="non-met"]').click();

                    }

                }
                if(organ1_params_json[4] != null){
                    if (organ1_params_json[4].type == "met"){
                        $('input:radio[name=type5][value="met"]').click();
                        if (organ1_params_json[4].const == "Linear"){
                            $("#const5").val("Linear");
                            }
                        if (organ1_params_json[4].const == "Menten"){
                            $("#const5").val("Menten");
                            }
                        $("#k_met5").val(organ1_params_json[4].k_met);
                        $("#k_bile5").val(organ1_params_json[4].k_bile);
                    }
                    if (organ1_params_json[4].type == "non-met"){
                        $('input:radio[name=type5][value="non-met"]').click();

                    }
                }


            }


        if(checked_res==1){
            $("#residual_selected").val('0');
            }
        else{
            $("#residual_selected").val('2');
            }

        if(checked_sk==1){
            $("#skin_selected").val('0');
            }
        else{
            $("#skin_selected").val('2');
            }
        if(checked_bla==1){
            $("#bladder_selected").val('0');
            }
        else{
            $("#bladder_selected").val('2');
            }
        if(checked_liv==1){
            $("#liver_selected").val('0');
            }
        else{
            $("#liver_selected").val('2');
            }
        if(checked_bl==1){
            $("#blood_selected").val('0');
            }
        else{
            $("#blood_selected").val('2');
            }
        if(checked_k==1){
            $("#kidney_selected").val('0');
            }
        else{
            $("#kidney_selected").val('2');
            }
        if(checked_lg==1){
            $("#lung_selected").val('0');
            }
        else{
            $("#lung_selected").val('2');
            }

        if(!$('#organ1').data('clicked')){
           $("#organ1_selected").val('2');
           }
        else{
            $("#organ1_selected").val('0');
        }
        if(!$('#organ2').data('clicked')){
           $("#organ2_selected").val('2');
           }
        else{
            $("#organ2_selected").val('0');
        }

        if(!$('#organ3').data('clicked')){
           $("#organ3_selected").val('2');
           }
        else{
            $("#organ3_selected").val('0');
        }
        if(!$('#organ4').data('clicked')){
           $("#organ4_selected").val('2');
           }
        else{
            $("#organ4_selected").val('0');
        }
        if(!$('#organ5').data('clicked')){
           $("#organ5_selected").val('2');
           }
        else{
            $("#organ5_selected").val('0');
        }
        if(checked_h==1){
            $("#heart_selected").val('0');
            }
        else{
            $("#heart_selected").val('2');
            }
        if(checked_m==1){
            $("#muscle_selected").val('0');
            }
        else{
            $("#muscle_selected").val('2');
            }
        if(checked_sp==1){
            $("#spleen_selected").val('0');
            }
        else{
            $("#spleen_selected").val('2');
            }
        if(checked_p==1){
            $("#placental_selected").val('0');
            }
        else{
            $("#placental_selected").val('2');
            }

        $(document).ready(function() {
            toggleFields(); //call this first so we start out with the correct visibility depending on the selected form values
           //this will call our toggleFields function every time the selection value of our field changes
            $("#resid").change(function() { toggleFields(); });

        });
        //this toggles the visibility of organ parameters.
        function toggleFields()
        {

            if ($("#skin_selected").val() < 1){
                $("#skinArea1").show();
                $('#s').parent().show();
                $( "#s" ).prop( "checked", true );
                }
            else{
                $("#skinArea1").hide();
                $('#s').parent().hide();
                }
            if ($("#residual_selected").val() < 1){
                $("#residualArea1").show();
                $('#r').parent().show();
                $( "#r" ).prop( "checked", true );
                }
            else{
                $("#residualArea1").hide();
                $('#r').parent().hide();
                }
            if ($("#bladder_selected").val() < 1){
                $("#bladderArea1").show();
                $('#bl').parent().show();
                $( "#bl" ).prop( "checked", true );

                }
            else{
                $("#bladderArea1").hide();
                $('#bl').parent().hide();
                }
            if ($("#liver_selected").val() < 1){
                $("#liverArea1").show();
                $('#li').parent().show();
                $( "#li" ).prop( "checked", true );
                }
            else{
                $("#liverArea1").hide();
                $('#li').parent().hide();
                }
            if ($("#blood_selected").val() < 1){
                $("#bloodArea1").show();
                $('#b').parent().show();
                $( "#b" ).prop( "checked", true );
                }
            else{
                $("#bloodArea1").hide();
                $('#b').parent().hide();
                }
            if ($("#lung_selected").val() < 1){
                $("#lungArea1").show();
                $('#l').parent().show();
                $( "#l" ).prop( "checked", true );
                }
            else{
                $("#lungArea1").hide();
                $('#l').parent().hide();
                }

            if ($("#kidney_selected").val() < 1){
                $("#kidneyArea1").show();
                $('#k').parent().show();
                $( "#k" ).prop( "checked", true );
                }
            else{
                $("#kidneyArea1").hide();
                $('#k').parent().hide();
                }
             if ($("#organ1_selected").val() < 1){
                $("#organ1Area1").show();
                $('#o1').parent().show();
                $('#organ1nam').show();
                $( "#o1" ).prop( "checked", true );
                }
            else{
                $("#organ1Area1").hide();
                $('#o1').parent().hide();
                $('#organ1nam').hide();

                }
             if ($("#organ2_selected").val() < 1){
                $("#organ2Area1").show();
                $('#o2').parent().show();
                $('#organ2nam').show();
                $( "#o2" ).prop( "checked", true );
                }
            else{
                $("#organ2Area1").hide();
                $('#o2').parent().hide();
                $('#organ2nam').hide();
                }
             if ($("#organ3_selected").val() < 1){
                $("#organ3Area1").show();
                $('#o3').parent().show();
                $('#organ3nam').show();
                $( "#o3" ).prop( "checked", true );
                }
            else{
                $("#organ3Area1").hide();
                $('#o3').parent().hide();
                $('#organ3nam').hide();
                }
             if ($("#organ4_selected").val() < 1){
                $("#organ4Area1").show();
                $('#o4').parent().show();
                $('#organ4nam').show();
                $( "#o4" ).prop( "checked", true );
                }
            else{
                $("#organ4Area1").hide();
                $('#o4').parent().hide();
                $('#organ4nam').hide();
                }
             if ($("#organ5_selected").val() < 1){
                $("#organ5Area1").show();
                $('#o5').parent().show();
                $('#organ5nam').show();
                $( "#o5" ).prop( "checked", true );
                }
            else{
                $("#organ5Area1").hide();
                $('#o5').parent().hide();
                $('#organ5nam').hide();
                }
            if ($("#heart_selected").val() < 1){
                $("#heartArea1").show();
                $('#h').parent().show();
                $( "#h" ).prop( "checked", true );
                }
            else{
                $("#heartArea1").hide();
                $('#h').parent().hide();
                }
            if ($("#muscle_selected").val() < 1){
                $("#muscleArea1").show();
                $('#m').parent().show();
                $( "#m" ).prop( "checked", true );
                }
            else{
                $("#muscleArea1").hide();
                $('#m').parent().hide();
                }
            if ($("#spleen_selected").val() < 1){
                $("#spleenArea1").show();
                $('#sp').parent().show();
                $( "#sp" ).prop( "checked", true );
                }
            else{
                $("#spleenArea1").hide();
                $('#sp').parent().hide();
                }
            if ($("#placental_selected").val() < 1){
                $("#placentalArea1").show();
                $('#pl').parent().show();
                $( "#pl" ).prop( "checked", true );
                }
            else{
                $("#placentalArea1").hide();
                $('#pl').parent().hide();
                }
        }


        dialogDrug.dialog( "open" );


        })

function draw_chart(organs_active, c) {
    var c_len= c.length;
                if($("#id_mod-method").val()  == "OpenLoop")
                    bl = c[1];
                else
                    bl = c[0];
                lu = c[3];
                var num=5;

                organs_active.push({
                            name: 'Blood',
                            data: bl,
                            yAxis: 1,
                        }, {
                            name: 'Lung',
                            data: lu,
                            yAxis: 1,
                        });

                if(checked_sk==1){
                    sk = c[num]
                    num=num+2;
                    organs_active.push({
                            name: 'Skin',
                            data:  sk,
                            yAxis: 1,
                        });
                }
                else{
                    sk=[]
                }
                if(checked_bla==1){
                    bla = c[num];
                    num=num+2;
                    organs_active.push({
                            name: 'Bladder',
                            data: bla,
                            yAxis: 1,
                        });
                }
                else{
                    bla=[]
                }
                if(checked_liv==1){
                    liv = c[num];
                    num=num+2;
                    organs_active.push({
                            name: 'Liver',
                            data:  liv,
                            yAxis: 1,
                        });
                }
                else{
                    liv=[]
                }
                if(checked_res==1){
                    res = c[num];
                    num=num+2;
                    organs_active.push({
                            name: 'Residual',
                            data:  res,
                            yAxis: 1,
                        });
                }
                else{
                    res=[]
                }
                if(checked_k==1){
                    ki = c[num];
                    num=num+2;
                    organs_active.push({
                            name: 'Kidney',
                            color: '#F1A9A0',
                            data:  ki,
                            yAxis: 1,
                        });
                }
                else{
                    ki=[]
                }
                if($('#organ1').data('clicked')){
                    organ1= c[num];
                    num=num+2;
                    organs_active.push({
                            name: $("#organ1").val() ,
                            color: '#00FFFF',
                            data:  organ1,
                            yAxis: 1,
                        });
                }
                else{
                    organ1=[]
                }
                if($('#organ2').data('clicked')){
                    organ2= c[num];
                    num=num+2;
                    organs_active.push({
                            name: $("#organ2").val(),
                            color: '#6666FF',
                            data:  organ2,
                            yAxis: 1,
                        });
                }
                else{
                    organ2=[]
                }
                if($('#organ3').data('clicked')){
                    organ3= c[num];
                    num=num+2;
                    organs_active.push({
                            name: $("#organ3").val(),
                            color: '#FFCC33',
                            data:  organ3,
                            yAxis: 1,
                        });
                }
                else{
                    organ3=[]
                }
                if($('#organ4').data('clicked')){
                    organ4= c[num];
                    num=num+2;
                    organs_active.push({
                            name: $("#organ4").val(),
                            color: '#00CC66',
                            data:  organ4,
                            yAxis: 1,
                        });
                }
                else{
                    organ4=[]
                }
                if($('#organ5').data('clicked')){
                    organ5= c[num];
                    num=num+2;
                    organs_active.push({
                            name: $("#organ5").val(),
                            color: '#3399FF',
                            data:  organ5,
                            yAxis: 1,
                        });
                }
                else{
                    organ5=[]
                }
                if(checked_h==1){
                    hear = c[num];
                    num=num+2;
                    organs_active.push({
                            name: 'Heart',
                            data:  hear,
                            yAxis: 1,
                        });
                }
                else{
                    hear=[]
                }
                if(checked_m==1){
                    mu = c[num]
                    num=num+2
                    organs_active.push({
                            name: 'Muscle',
                            data:  mu,
                            yAxis: 1,
                        });
                }
                else{
                    mu=[]
                }
                if(checked_sp==1){
                    sp = c[num]
                    num=num+2
                    organs_active.push({
                            name: 'Spleen',
                            color: '#1BBC9B',
                            data:  sp,
                            yAxis: 1,
                        });
                }
                else{
                    sp=[]
                }
                if(checked_p==1){
                    place = c[num];
                    num=num+2;
                    organs_active.push({
                            name: 'Placental',
                            color: '#CC00CC',
                            data:  place,
                            yAxis: 1,

                        });
                }
                else{
                    place=[]
                }

    $('#below').highcharts({
                    title: {
                        text: 'Expected response of the system',
                        x: -20 //center,
                    },

                    xAxis: {
                       title: {
                            text: 'Time (hr)'
                        },
                    },
                    yAxis: [{
                            height: 150,
                            min: 0,
                            title: {
                                text: 'Administration Rate (g/hr)'
                            },
                            labels: {
                                format: '{value:.2f}',
                                formatter: function() {
                                 return parseFloat((this.value));
                                }
                            },

                            plotLines: [{
                            value: 0,
                            width: 1,
                            color: '#808080'
                        }],

                        }, {
                            title: {
                                text: 'State variables (g/L)'
                            },
                            labels: {

                                formatter: function() {
                                return this.value.toExponential();
                                //return parseFloat((this.value));
                                }
                            },
                            plotLines: [{
                            value: 0,
                            width: 1,
                            color: '#808080'
                        }],
                            //tickInterval: 0.0000001,
                            min: 0,
                            top: 230,
                            height: 100,
                            offset: 0,
                            //lineWidth: 2
                        }],

                    tooltip: {
                        formatter: function() {
                            return '<b>'+  this.y.toExponential(2) +'</b><br/>'+
                                'Time: '+ Highcharts.numberFormat(this.x, 2);
                        }

                    },
                    legend: {
                        layout: 'vertical',
                        align: 'right',
                        verticalAlign: 'middle',
                        borderWidth: 0
                    },
                    series: organs_active
                });
}

if (typeof(ModelForm.json) != "undefined") {
	organs_active = [{
                            name: 'Administration rate',
                            data: JSON.parse(ModelForm.adm),
                            step: true
                        }];

    draw_chart(organs_active, JSON.parse(ModelForm.json));
}
else if (ModelForm.edit || ModelForm.image) {
    var organs_active, model_source;
    //id_mod-plot_params

    $.ajax({
        url: '/get_step_params/' + ModelForm.pk,
        success: function(data) {
            $("#id_mod-step_params").val(data);
            var admin_rate = JSON.parse($("#id_mod-step_params").val() );
            organs_active = [{
                            name: 'Administration rate',
                            data: JSON.parse(admin_rate),
                            step: true
                        }];

		    }
	});

	 $.ajax({
            url: '/get_plot_params/' + ModelForm.pk,
            success: function(data) {
                $("#id_mod-plot_params").val(data);
                var c = JSON.parse($("#id_mod-plot_params").val());
                draw_chart(organs_active, c);
            }
        });

}

//if default don't change color on hover
    if (ModelForm.default) {
        $('#heart').removeClass( "enabled" )
        $('#muscle').removeClass( "enabled" )
        $('#spleen').removeClass( "enabled" )
        $('#placental').removeClass( "enabled" )
    }


//MPC dialog


			dialogSet = $( "#dialog-setpoint" ).dialog({
				autoOpen: false,
				modal: true,
				width: 808,
				height: 520,
				left: 300,
				top: 200,
				buttons: {
				"Save changes":{
				    text: "Save changes",
			        id: "closeloop-save",
					click: function() {

                        //set time same as end time of the last field
                        var i=$('#inter').val()-1;
                        var option_result = $('#txt_close'+i).val();
                        var option_array=option_result.split("-");
                        $('#total_t').val(eval(option_array[1]));

                        interval = $('#inter').val();
                        var list_setpoint=[]
                        var list_time_close=[]
                        var list_end=[]
                        for( var i=0; i<interval ;i++) {
                             if ($('#txtbox_close'+i).length){
                                list_setpoint[i]=$('#txtbox_close'+i).val()
                                var option_result = $('#txt_close'+i).val();
                                var option_array=option_result.split("-");
                                list_time_close[i] = option_array[0];
                                list_end[i] = option_array[1];
                                }
                        }
                        //create json from values
                        var params_json = {
                            N: $("#Np").val(),
                            intervals: $("#inter").val(),
                            step: $("#step_p").val(),
                            end: $("#total_t").val(),
                            time: list_time_close,
                            setpoint: list_setpoint,
                            time_int_final: list_end,
                            Q : $("#q_weight").val(),
                            R : $("#r_weight").val(),
                        };
                        //check closeloop function
                        check_closeloop();
                        //pass json to field to be read by the view
                        $("#id_mod-method_params").val( JSON.stringify(params_json) );


					}
				},
				}
			});


			dialogOpen = $( "#dialog-open" ).dialog({
				autoOpen: false,
				modal: true,
				width: 808,
				height: 520,
				left: 300,
				top: 200,
				buttons: {
				"Save changes":{
                    text: "Save changes",
				    id: "openloop-save",
				    'class': "btn-op-save",
					click: function() {
					    //set time same as end time of the last field
                        var i=$('#N_int').val()-1;
                        var option_result = $('#txt'+i).val();
                        var option_array=option_result.split("-");
                        $('#Time').val(eval(option_array[1]));
						openloop_send_vals();
						check();

					}
					}
				},
			});

    //check if form is valid
        function check_closeloop(){
             var a = document.getElementById('inter').value;
             var t = $('#total_t').val();
             var prev="0";
             var er=0;
             var list_time=[]
             var list_time2=[]
              for( var i=0; i<a ;i++) {
                if ($('#txtbox_close'+i).length){
                    var option_result = $('#txt_close'+i).val();
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
                    if (parseInt(list_time[i]) > parseInt(list_time2[i])){
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
                $("#id_mod-method").val('CloseLoop-MPC');
                dialogSet.dialog( "close" );
                }

            }

//Tutorial -->

    if (ModelForm.tutorial) {

        if (ModelForm.tutorial_result) {

              var trip11 = new Trip([
              {sel : $(".below"), content : "You can print and download the produced graph.", position : "n", delay:3000 , },
              {sel : $(".below"), content : "You can add and remove organs from graph by clicking on label.", position : "e", delay:3000 , },
              {sel : $(".simulation-parameters"), position:"e", content : "You can also run the default model using openloop simulation. <br> Click <span style='color: #1abc9c'>Simulation Parameters -> OpenLoop</span> ", position : "e", delay:-1 , onTripChange:  function (tripIndex, tripObject){$('#open').on('click', function() {if ( tripIndex === 2 ) {trip12.start();}}) },  },
              ],{

              });
              var trip12 = new Trip([
              {sel : $(".fields"), position:"e", content : "Fill in the field Total Time with 10 and the field Number of Intervals with 4.<br> Next click <span style='color: #1abc9c'>Submit.</span> ", position : "e", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#submit_open').on('click', function() { if ($('#N_int').val() == 4 && $('#Time').val() == 10 ){trip13.start();}  });  $('#openloop-save').on('click', function() { if ($('#N_int').val() != 4 && $('#Time').val() != 10 ){ dialogOpen.dialog( "open" ); } })  },  },
              ],{

              });
              var trip13 = new Trip([
              {sel : $(".tut-table"), position:"e", content : "As you can see the drug dosage is 2 g/hr for each time of interval.<br>Change it from  2 to 0 for 2.5-5 sec. </br> Next, click Save changes. ", position : "e", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#openloop-save').on('click', function() { if ($('#txtbox1').val() == 0 ){trip14.start();} else { dialogOpen.dialog( "open" );} }) },  },

              ],{

              });
              var trip14 = new Trip([
              { sel : $(".create"), content : "Now, click again <span style='color: #1abc9c'>Create model</span> to run the default model.", position : "e", delay:-1,  onTripChange:  function (tripIndex, tripObject){$('#Create_model').on('click', function() {trip14.next();}) }, },
              ],{

              });

            $(document).ready(function() {
                trip11.start();
            });
    } else if (ModelForm.tutorial_openloop_result) {

         var trip15 = new Trip([
          {sel : $(".below"), content : "Above you can see the results of openloop simulation.", position : "n", delay:3000 , },
          {sel : $(".below"), content : "Congratulations!<br>You have learnt to simulate the default model.", delay:5000 , },
          ],{

          });

          $(document).ready(function()
             {
              trip15.start();
            });

    } else {
    var trip1 = new Trip([
          { sel : $(".form-table"), content : "<h>Welcome to pbpk!</h><br>At the end of this tutorial you can run the default model.<br>Above you can see modelname, BW, hematocrit, CO.", position : "n", showNavigation : true,showCloseBox : true, delay:-1 },
          { sel : $(".lung"), content : "Below you can see the organs included to default model.", position : "n", showNavigation : true,showCloseBox : true, delay:-1 },
          { sel : $(".blood"), content : "Click on <span style='color: #1abc9c'>blood</span> to see blood parameters.", position : "n", delay:-1 ,  onTripChange:  function (tripIndex, tripObject){ $('#blood').on('click', function() {if ( tripIndex === 2 ) {trip1.next();} } )},},
          { position: 'screen-center',content : "You can see blood volume. Click <b><span style='color: #1abc9c'>OK</span></b> to proceed.", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#blood-ok').on('click', function() {if ( tripIndex === 3 ) { trip2.start();}})   }, },

        ],{
          delay: 1000,
          onTripPause : function (tripIndex, tripObject){
            setInterval(tripObject,3000);
            console.log('pause : ', tripIndex);

          },

          onTripChange : function (i, tripData) {
          console.log("current tripIndex1 : " + i);
            }
        });
        var trip2 = new Trip([
          { sel : $(".lung"),content : "Click on <span style='color: #1abc9c'>lung</span> to see lung parameters.",  position : "n", delay:-1 , onTripChange:  function (tripIndex, tripObject){ if ( tripIndex === 0 ) { $('#lung').on('click', function() {if ($("#dialog-lung").dialog( "isOpen" )){trip2.next();} } ) } }, },
          {sel : $(".lung-dialog"), position: "n", content : "<h>You can see lung flow, lung volume and blood in lung.</h><br> Click <span style='color: #1abc9c'>OK</span> to proceed.", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#lung-ok').on('click', function() {if ( tripIndex === 1 ) {trip8.start();}}) }, },
          ],{
            onTripChange : function (i, tripData) {
            }
            });
        var trip8 = new Trip([
          { sel : $(".drug-properties"), content : "Click on <span style='color: #1abc9c'>Define Drug Properties</span>.", position : "e", delay:-1 ,onTripChange:  function (tripIndex, tripObject){ $('#drug').on('click', function() {if ( tripIndex === 0 ) {trip8.next();} } ) },
           },
          {sel : $(".drug-dialog"),position: "n", content : "You can see drug properties.", delay:1000 ,  },
          {sel : $(".drug-dialog"),position: "e", content : "Scroll down to see drug properties for all included organs.<br> Click <span style='color: #1abc9c'>OK</span> to proceed.", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#drug-ok').on('click', function() {if ( tripIndex === 2 ) {trip9.start();}}) }, },

          ],{
          onTripChange : function (i, tripData) {
          }

          });
        var trip9 = new Trip([

          { sel : $(".simulation-parameters"), content : "Click on Simulation Parameters and select <span style='color: #1abc9c'>Model Predictive Control</span>.", position : "e", delay: -1, onTripChange:  function (tripIndex, tripObject){$('#mpc').on('click', function() {if ( tripIndex === 0 ) {trip10.start();}}) },},

          ],{
          onTripChange : function (i, tripData) {
          }

          });
           var trip10 = new Trip([
              {sel : $(".closeloop-dialog"), position: "e",content : "Click <span style='color: #1abc9c'>Save changes</span>.", delay:-1 , onTripChange:  function (tripIndex, tripObject){$('#closeloop-save').on('click', function() {if ( tripIndex === 0 ) {trip10.next();}}) }, },
              //{ sel : $(".ui-button-text"), content : "Click <span style='color: #1abc9c'>Save</span>.", position : "e" },
              { sel : $(".create"), content : "Click <span style='color: #1abc9c'>Create model</span> to run the default model.", position : "e", delay:-1,  onTripChange:  function (tripIndex, tripObject){$('#Create_model').on('click', function() {if ( tripIndex === 0 ) {trip10.next();}}) }, },
              ],{
              onTripChange : function (i, tripData) {
              }

            });


        $(document).ready(function()
         {
          trip1.start();
        });
    }
}

if (ModelForm.t_create) {
    var trip1 = new Trip([
      { sel : $(".form-table"), content : "In this tutorial you will create a new model.<br>Above you can see default BW and hematocrit.<br> Please enter name <b><span style='color: #1abc9c'>test model</span></b> for your model.", position : "n", showCloseBox : true, delay:-1, onTripChange:  function (tripIndex, tripObject){ $('#id_mod-modelname').on('change', function() {if (  $('#id_mod-modelname').val() == "testmodel" ){ trip1.next();}})  }, },
      { sel : $("#id_mod-cardiac_output"), content : "Enter <b><span style='color: #1abc9c'>16.0</span></b>  to CO.", position : "e", delay:-1, onTripChange:  function (tripIndex, tripObject){ $('#id_mod-cardiac_output').on('change', function() {if (  $('#id_mod-cardiac_output').val() == "16.0"  ){ trip1.next();}})  }, },
      { sel : $(".blood"), content : "Click on <span style='color: #1abc9c'>blood</span> to add blood parameters.", position : "n", delay:-1 ,  onTripChange:  function (tripIndex, tripObject){ $('#blood').on('click', function() {if ( tripIndex === 2 ) {trip1.next();} } )},},
      { position: 'screen-center',content : "Fill in blood volume with 0.5.", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#blo_v_f').on('change', function() {if ( $('#blo_v_f').val()  == 0.5 ) { trip1.next();}})   }, },
      { sel :  $("#blo_v_f") ,content : "Click <b><span style='color: #1abc9c'>Save Changes</span></b> to proceed.", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#blood-sv').on('click', function() {  trip1.next();})   }, },
      { sel : $(".lung"), content : "Click on <span style='color: #1abc9c'>lung</span> to add lung parameters.", position : "n", delay:-1 ,  onTripChange:  function (tripIndex, tripObject){ $('#lung').on('click', function() { trip1.next();} )},},
      { sel :  $("#lg_f_f"), content : "Fill in lung flow with 1.0", position : "n", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#lg_f_f').on('change', function() {if ( $('#lg_f_f').val()  == 1.0 ) { trip1.next();}})   }, },
      { sel :  $("#lg_v_f"), content : "Fill in lung volume with 0.007", position : "n", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#lg_v_f').on('change', function() {if ( $('#lg_v_f').val()  == 0.007 ) { trip1.next();}})   }, },
      { sel :  $("#lg_b_f"), content : "Fill in blood in lung 0.5.", position : "n", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#lg_b_f').on('change', function() {if ( $('#lg_b_f').val()  == 0.5 ) { trip1.next();}})   }, },
      { sel :  $("#lg_b_f") ,content : "Click <b><span style='color: #1abc9c'>Save Changes</span></b> to proceed.", delay:-1 ,onTripChange:  function (tripIndex, tripObject){ $('#lung-sv').on('click', function() {  trip1.next();})  }, },
      { sel : $(".kidney"), content : "Click on <span style='color: #1abc9c'>kidney</span> to add lung parameters.", position : "n", delay:-1 ,  onTripChange:  function (tripIndex, tripObject){ $('#kidney').on('click', function() { trip1.next();} )},},
      { sel :  $("#kid_f_f"), content : "Fill in kidney flow with 0.091", position : "n", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#kid_f_f').on('change', function() {if ( $('#kid_f_f').val()  == 0.091 ) { trip1.next();}})   }, },
      { sel :  $("#kid_v_f"), content : "Fill in kidney volume with 0.017", position : "n", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#kid_v_f').on('change', function() {if ( $('#kid_v_f').val()  == 0.017 ) { trip1.next();}})   }, },
      { sel :  $("#kid_b_f"), content : "Fill in blood in kidney 0.24. Click <b><span style='color: #1abc9c'>Save Changes</span></b> to proceed.", position : "n", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#kid_b_f').on('change', function() {if ( $('#kid_b_f').val()  == 0.24 ) { trip1.next();}})   }, },
      { sel :  $("#kid_b_f") ,content : "Click <b><span style='color: #1abc9c'>Save Changes</span></b> to proceed.", delay:-1 ,onTripChange:  function (tripIndex, tripObject){ $('#kidney-sv').on('click', function() {  trip1.next();})  }, },
      { sel : $(".residual"), content : "Click on <span style='color: #1abc9c'>residual</span> to add residual parameters.", position : "n", delay:-1 ,  onTripChange:  function (tripIndex, tripObject){ $('#residual').on('click', function() { trip1.next(); } )},},
      { position: 'screen-center',content : "Fill in blood volume with 0.04.", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#res_b_f').on('change', function() {if ( $('#res_b_f').val()  == 0.04 ) { trip1.next();}})   }, },
      { position: 'screen-center' ,content : "Click <b><span style='color: #1abc9c'>Save Changes</span></b> to proceed.", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#res-sv').on('click', function() {  trip1.next();})   }, },
      { sel :  $(".drug-properties") , position : "s",content : "Click on <b><span style='color: #1abc9c'>Define drug properties</span></b>.", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#drug').on('click', function() {  trip1.next();})   }, },
      { sel :  $("#drugname") ,content : "Fill in <b><span style='color: #1abc9c'>drugname</span></b> with drugtest.", delay:-1 , position : "e", onTripChange:  function (tripIndex, tripObject){ $('#drugname').on('change', function() { if ( $('#drugname').val()  == "drugtest" ) trip1.next();})   }, },
      { sel :  $("#max_influx") ,content : "Fill in <b><span style='color: #1abc9c'>Maximum Influx Rate</span></b> with 4e-8.", delay:-1 , position : "e", onTripChange:  function (tripIndex, tripObject){ $('#max_influx').on('change', function() { if ( $('#max_influx').val()  == "4e-8" ) trip1.next();})   }, },
      { sel :  $("#p_rest") ,content : "Fill in <b><span style='color: #1abc9c'>P</span></b> with 1.6.", delay:-1 , position : "e", onTripChange:  function (tripIndex, tripObject){ $('#p_rest').on('change', function() { if ( $('#p_rest').val()  == "1.6" ) trip1.next();})   }, },
      { sel :  $("#pi_rest") ,content : "Fill in <b><span style='color: #1abc9c'>π</span></b> with 0.0095.", delay:-1 , position : "e", onTripChange:  function (tripIndex, tripObject){ $('#pi_rest').on('change', function() { if ( $('#pi_rest').val()  == "0.0095" ) trip1.next();})   }, },
      { sel :  $("#p_kid") ,content : "Fill in <b><span style='color: #1abc9c'>P</span></b> with 0.14.", delay:-1 , position : "e", onTripChange:  function (tripIndex, tripObject){ $('#p_kid').on('change', function() { if ( $('#p_kid').val()  == "0.14" ) trip1.next();})   }, },
      { sel :  $("#pi_kid") ,content : "Fill in <b><span style='color: #1abc9c'>π</span></b> with 0.12.", delay:-1 , position : "e", onTripChange:  function (tripIndex, tripObject){ $('#pi_kid').on('change', function() { if ( $('#pi_kid').val()  == "0.12" ) trip1.next();})   }, },
      { sel :  $("#kin_kidney") ,content : "Fill in <b><span style='color: #1abc9c'>k_kidney</span></b> with 0.0164.", delay:-1 , position : "e", onTripChange:  function (tripIndex, tripObject){ $('#kin_kidney').on('change', function() { if ( $('#kin_kidney').val()  == "0.0164" ) trip1.next();})   }, },
      { sel :  $("#pi_rb") ,content : "Fill in <b><span style='color: #1abc9c'>Pi Red Blood Cells</span></b> with 1.3.", delay:-1 , position : "e", onTripChange:  function (tripIndex, tripObject){ $('#pi_rb').on('change', function() { if ( $('#pi_rb').val()  == "1.3" ) trip1.next();})   }, },
      { sel :  $("#pi_pl") ,content : "Fill in <b><span style='color: #1abc9c'>Pi Plasma</span></b> with 0.81.", delay:-1 , position : "e", onTripChange:  function (tripIndex, tripObject){ $('#pi_pl').on('change', function() { if ( $('#pi_pl').val()  == "0.81" ) trip1.next();})   }, },
      { sel :  $("#p_lg") ,content : "Fill in <b><span style='color: #1abc9c'>P</span></b> with 0.44.", delay:-1 , position : "e", onTripChange:  function (tripIndex, tripObject){ $('#p_lg').on('change', function() { if ( $('#p_lg').val()  == "0.44" ) trip1.next();})   }, },
      { sel :  $("#pi_lg") ,content : "Fill in <b><span style='color: #1abc9c'>π</span></b> with 0.94.", delay:-1 , position : "e", onTripChange:  function (tripIndex, tripObject){ $('#pi_lg').on('change', function() { if ( $('#pi_lg').val()  == "0.94" ) trip1.next();})   }, },
      { sel : $(".simulation-parameters"), content : "Click on Simulation Parameters and select <span style='color: #1abc9c'>Model Predictive Control</span>.", position : "e", delay: -1, onTripChange:  function (tripIndex, tripObject){$('#mpc').on('click', function() { trip1.next();}) },},
      { sel : $(".closeloop-dialog"), position: "e",content : "Click <span style='color: #1abc9c'>Save changes</span>.", delay:-1 , onTripChange:  function (tripIndex, tripObject){$('#closeloop-save').on('click', function() { trip1.next();}) }, },
      { sel : $(".create"), content : "Click <span style='color: #1abc9c'>Create model</span> to run the default model.", position : "s", delay:-1,  onTripChange:  function (tripIndex, tripObject){$('#Create_model').on('click', function() { trip2.start();}) }, },
    ],{
      delay: 1000,
      onTripPause : function (tripIndex, tripObject){
        setInterval(tripObject,3000);
        console.log('pause : ', tripIndex);

      },

      onTripChange : function (i, tripData) {
      console.log("current tripIndex1 : " + i);
        }
    });
    var trip2 = new Trip([
      { sel : $(".lung"),content : "Click on <span style='color: #1abc9c'>lung</span> to see lung parameters.",  position : "n", delay:-1 , onTripChange:  function (tripIndex, tripObject){ if ( tripIndex === 0 ) { $('#lung').on('click', function() {if ($("#dialog-lung").dialog( "isOpen" )){trip2.next();} } ) } }, },
      {sel : $(".lung-dialog"), position: "n", content : "<h>You can see lung flow, lung volume and blood in lung.</h><br> Click <span style='color: #1abc9c'>OK</span> to proceed.", delay:-1 , onTripChange:  function (tripIndex, tripObject){ $('#lung-ok').on('click', function() {if ( tripIndex === 1 ) {trip8.start();}}) }, },
      ],{
        onTripChange : function (i, tripData) {
        }
        });
    $(document).ready(function()
     {
      trip1.start();
    });
} else if (ModelForm.t_create_final) {
    var trip2 = new Trip([
      {sel : $(".below"), content : "Above you can see the results of model predictive control simulation.", position : "n", delay:3000 , },
      {sel : $(".below"), content : "Congratulations!<br>You have learnt to create new model.", delay:5000 , },
      ],{

      });

      $(document).ready(function()
         {
          trip2.start();
        });
}
});

var p = $( "#Blood2" );
            var BloodPos = p.position();
            var p1 = $( "#skin" );
            var SkinPos = p1.position();
            var p2 = $( "#kidney" );
            var KidPos = p2.position();
            var p3 = $( "#bladder" );
            var BlPos = p3.position();
            var p4 = $( "#liver" );
            var LivPos = p4.position();
            var p5 = $( "#lung" );
            var LungPos = p5.position();
            var p6 = $( "#residual" );
            var ResPos = p6.position();
            var p7 = $( "#blood" );
            var BloPos = p7.position();
            var p8= $("#div-placental");
            var Org1Pos= p8.position();
            var p9 = $( "#heart" );
            var HeartPos = p9.position();
            var p10 = $( "#muscle" );
            var MusclePos = p10.position();
            var p11 = $( "#spleen" );
            var SplPos = p11.position();
            var p13 = $( "#placental" );
            var PlPos = p13.position();


//Canvas-Position of darts\

            //Add darts
            //Lung
			var c = document.getElementById("canvas");
			var ctx1 = c.getContext("2d");

            //Lung darts
			function lung(){

			    var c = document.getElementById("canvas");
			    var ctx1 = c.getContext("2d");

                ctx1.moveTo((p.width()/2)+BloodPos.left,LungPos.top+p2.height()-92);
                ctx1.lineTo((p.width()/2)+BloodPos.left,BloodPos.top-92);
                ctx1.stroke();

                var ctx1 = c.getContext("2d");
                ctx1.moveTo(LungPos.left,LungPos.top+p2.height()-92);
                ctx1.lineTo((p.width()/2)+BloodPos.left,LungPos.top+p2.height()-92);
                ctx1.stroke();

                var ctx1 = c.getContext("2d");
                ctx1.moveTo(LungPos.left-10,LungPos.top+p2.height()-92);
                ctx1.lineTo(LungPos.left-20,LungPos.top+p2.height()-5-92);
                ctx1.stroke();

                var ctx1 = c.getContext("2d");
                ctx1.moveTo(LungPos.left-10,LungPos.top+p2.height()-92);
                ctx1.lineTo(LungPos.left-20,LungPos.top+p2.height()+5-92);
                ctx1.stroke();

                ctx1.moveTo(BloPos.left+12+(p7.width()/2),LungPos.top-92+p2.height());
                ctx1.lineTo(LungPos.left+12+p2.width(),LungPos.top-92+p2.height());
                ctx1.stroke();

                ctx1.moveTo(BloPos.left+12+(p7.width()/2),BloodPos.top-92);
                ctx1.lineTo(BloPos.left+12+(p7.width()/2),LungPos.top-92+p2.height());
                ctx1.stroke();

                ctx1.moveTo(BloPos.left+12+(p7.width()/2)-5,BloodPos.top-10-92);
                ctx1.lineTo(BloPos.left+12+(p7.width()/2),BloodPos.top-92);
                ctx1.stroke();

                ctx1.moveTo(BloPos.left+12+(p7.width()/2)+5,BloodPos.top-10-92);
                ctx1.lineTo(BloPos.left+12+(p7.width()/2),BloodPos.top-92);
                ctx1.stroke();
            }

            //Darts for kidney, bladder, skin, residual
            function organ_dart(organ){

                ctx1.moveTo(organ.position().left,organ.position().top-92+organ.height());
                ctx1.lineTo(BloodPos.left+p1.width(),organ.position().top-92+organ.height());
                ctx1.stroke();

                ctx1.moveTo(BloPos.left,organ.position().top-92+organ.height());
                ctx1.lineTo(organ.position().left+14+p1.width(),organ.position().top-92+organ.height());
                ctx1.stroke();

                //belos

                ctx1.moveTo(organ.position().left+24+p1.width(),organ.position().top-92+organ.height()+5);
                ctx1.lineTo(organ.position().left+14+p1.width(),organ.position().top-92+organ.height());
                ctx1.stroke();

                ctx1.moveTo(organ.position().left+24+p1.width(),organ.position().top-92+organ.height()-5);
                ctx1.lineTo(organ.position().left+14+p1.width(),organ.position().top-92+organ.height());
                ctx1.stroke();

                ctx1.moveTo(BloodPos.left+p1.width()+13,organ.position().top-92+organ.height()+5);
                ctx1.lineTo(BloodPos.left+p1.width()+3,organ.position().top-92+organ.height());
                ctx1.stroke();

                ctx1.moveTo(BloodPos.left+p1.width()+13,organ.position().top-92+organ.height()-5);
                ctx1.lineTo(BloodPos.left+p1.width()+3,organ.position().top-92+organ.height());
                ctx1.stroke();
                }



            //Liver Darts
            function liver(){
                ctx1.moveTo(LivPos.left,LivPos.top-92+p3.height());
                ctx1.lineTo(BloodPos.left+p1.width(),LivPos.top-92+p2.height());
                ctx1.stroke();

                ctx1.moveTo(BloPos.left,LivPos.top-92+p3.height());
                ctx1.lineTo(LivPos.left+14+p4.width(),LivPos.top-92+p2.height());
                ctx1.stroke();

                //liver-belos

                ctx1.moveTo(LivPos.left+24+p4.width(),LivPos.top-92+p2.height()+5);
                ctx1.lineTo(LivPos.left+14+p4.width(),LivPos.top-92+p2.height());
                ctx1.stroke();

                ctx1.moveTo(LivPos.left+24+p4.width(),LivPos.top-92+p2.height()-5);
                ctx1.lineTo(LivPos.left+14+p4.width(),LivPos.top-92+p2.height());
                ctx1.stroke();

                ctx1.moveTo(BloodPos.left+p1.width()+13,LivPos.top-92+p2.height()+5);
                ctx1.lineTo(BloodPos.left+p1.width()+3,LivPos.top-92+p2.height());
                ctx1.stroke();

                ctx1.moveTo(BloodPos.left+p1.width()+13,LivPos.top-92+p2.height()-5);
                ctx1.lineTo(BloodPos.left+p1.width()+3,LivPos.top-92+p2.height());
                ctx1.stroke();
                }

                // Added organs darts

			function neworgan(left,top){

					ctx1.moveTo(left,top-92+p3.height());
					ctx1.lineTo(BloodPos.left+p1.width(),top-92+p2.height());
					ctx1.stroke();

					ctx1.moveTo(BloPos.left,top-92+p3.height());
					ctx1.lineTo(BlPos.left+19+p1.width(),top-92+p2.height());
					ctx1.stroke();

					//residual-belos

					ctx1.moveTo(BlPos.left+29+p1.width(),top-92+p2.height()-5);
					ctx1.lineTo(BlPos.left+19+p1.width(),top-92+p2.height());
					ctx1.stroke();

					ctx1.moveTo(BlPos.left+29+p1.width(),top-92+p2.height()+5);
					ctx1.lineTo(BlPos.left+19+p1.width(),top-92+p2.height());
					ctx1.stroke();

					ctx1.moveTo(BloodPos.left+p1.width()+13, top-92+p2.height()+5);
					ctx1.lineTo(BloodPos.left+p1.width()+3, top-92+p2.height());
					ctx1.stroke();

					ctx1.moveTo(BloodPos.left+p1.width()+13, top-92+p2.height()-5);
					ctx1.lineTo(BloodPos.left+p1.width()+3, top-92+p2.height());
					ctx1.stroke();

					}

