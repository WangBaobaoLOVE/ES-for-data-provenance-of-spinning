create database mashan;
use mashan;
create table cusha (
	record_id bigint not null auto_increment,
	machineNo int,
	record_timestamp datetime,
	spindle_speed_set int,
	spindle_speed_full_yarn int,
	raw_head_speed int,
	draft_ratio decimal(9,2),
	character_coeff decimal(20,2),
	bobbin_coeff decimal(20,2),
	layer_thickness decimal(20,2),
	roving_twist decimal(20,2),
	bobbin_diameter decimal(20,2),
	fixed_length int,
	roving_quantity int,
	pressure_palm_laps int,
	winding_density decimal(20,2),
	form_length int,
	form_angle int,
	reversing_forbid int,
	intubation_position int,
	raw_head_position int,
	stop_position int,
	top_correction int,
	bottom_correction int,
	above_keel_refueling_time_interval int,
	below_keel_refueling_time_interval int,
	nozzle_filling_duration int,
	cone_top_position int,
	dolly_position int,
	take_full_yarn_above_reversing_position int,
	take_full_yarn_below_stop_position int,
	release_full_yarn_above_reversing_position int,
	release_full_yarn_below_stop_position int,
	take_black_bobbin_below_stop_position int,
	take_black_bobbin_above_reversing_position int,
	shake_position int,
	release_black_bobbin_below_stop_position int,
	release_black_bobbin_above_reversing_position int,
	stop_length int,
	return_yarn_length int,
	winding_position int,
	immediate_full_yarn_return_length int,
	advance_parking_length int,
	forbid_adjustment_coeff int,
	blow_suction_air_motor_interval_time int,
	blow_suction_air_motor_continue_time int,
	doffing_process_setting int,
	full_yarn_return_yarn_coeff int,
	full_yarn_twisting_time int,
	PRIMARY KEY ( record_id ));
