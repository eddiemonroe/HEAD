#********************************************************************************************************************************************
    
    def childGenerator_cutandspliceGA(self):
        
        # an array that holds list of the rate values as defined in the blenderPlayback.py
        rates_scene = [bpy.data.scenes['Scene'].rate1, bpy.data.scenes['Scene'].rate2, bpy.data.scenes['Scene'].rate3, bpy.data.scenes['Scene'].rate4, bpy.data.scenes['Scene'].rate5, bpy.data.scenes['Scene'].rate6, bpy.data.scenes['Scene'].rate7, bpy.data.scenes['Scene'].rate8, bpy.data.scenes['Scene'].rate9, bpy.data.scenes['Scene'].rate10, bpy.data.scenes['Scene'].rate11, bpy.data.scenes['Scene'].rate12, bpy.data.scenes['Scene'].rate13, bpy.data.scenes['Scene'].rate14, bpy.data.scenes['Scene'].rate15, bpy.data.scenes['Scene'].rate16, bpy.data.scenes['Scene'].rate17, bpy.data.scenes['Scene'].rate18, bpy.data.scenes['Scene'].rate19, bpy.data.scenes['Scene'].rate20, bpy.data.scenes['Scene'].rate21, bpy.data.scenes['Scene'].rate22, bpy.data.scenes['Scene'].rate23, bpy.data.scenes['Scene'].rate24, bpy.data.scenes['Scene'].rate25, bpy.data.scenes['Scene'].rate26, bpy.data.scenes['Scene'].rate27, bpy.data.scenes['Scene'].rate28, bpy.data.scenes['Scene'].rate29, bpy.data.scenes['Scene'].rate30, bpy.data.scenes['Scene'].rate31, bpy.data.scenes['Scene'].rate32, bpy.data.scenes['Scene'].rate33, bpy.data.scenes['Scene'].rate34, bpy.data.scenes['Scene'].rate35, bpy.data.scenes['Scene'].rate36]

############################################################################################################################################################
# First initialize the variables of the rate values with any value. The purpose is to be able to put them into the 'items_var' array and assign them each of values of the 'rate_scene'(which are rate values assigned by the user) array using the for-loop given below.
############################################################################################################################################################
        rate1_val=1; rate2_val=1; rate3_val=1; rate4_val=1; rate5_val=1; rate6_val=1; rate7_val=1; rate8_val=1; rate9_val=1; rate10_val=1;  rate11_val=1; rate12_val=1; rate13_val=1; rate14_val=1; rate15_val=1; rate16_val=1; rate17_val=1; rate18_val=1; rate19_val=1; rate20_val=1; rate21_val=1; rate22_val=1; rate23_val=1; rate24_val=1; rate25_val=1; rate26_val=1; rate27_val=1; rate28_val=1; rate29_val=1; rate30_val=1; rate31_val=1; rate32_val=1; rate33_val=1; rate34_val=1; rate35_val=1; rate36_val=1
# collect all the default initialized rate values in the 'rates_var' array
        rates_var=[rate1_val,rate2_val,rate3_val,rate4_val,rate5_val,rate6_val,rate7_val,rate8_val,rate9_val,rate10_val,rate11_val,rate12_val,rate13_val,rate14_val,rate15_val,rate16_val, rate17_val, rate18_val, rate19_val, rate20_val, rate21_val,rate22_val, rate23_val, rate24_val, rate25_val,rate26_val, rate27_val, rate28_val,rate29_val, rate30_val, rate31_val, rate32_val,rate33_val, rate34_val, rate35_val, rate36_val]
#re-assign 'rates_var' members with rate values, the user assigned, as extracted from the 'rates_scene' array.
        for i in range(0, len(rates_scene)):
            rates_var[i]= rates_scene[i]
        par_values = []
############################################################################################################################################################
# Only rate values that range between 1 and 6 will be considered for breeding. Eventhough currently, no algorithm is included to make breeding #more degree specific between the six different rate values for breeding. In other words all values(b/n 1 and 6) are considered similar during breeding. Actions rated zero(0) are mutated.
############################################################################################################################################################
        for items in range(0, len(rates_var)):
            if 1 <= rates_var[items] <= 6:
                par_values.append(rates_var[items])

        p1= 0; p2= 0; p3= 0; p4= 0; p5= 0; p6= 0; p7= 0; p8= 0; p9= 0; p10= 0; p11= 0; p12= 0; p13= 0; p14= 0; p15= 0; p16= 0; p17= 0; p18= 0; p19= 0; p20= 0; p21= 0; p22= 0; p23= 0; p24= 0;
        p25= 0; p26= 0; p27= 0; p28= 0; p29= 0; p30= 0; p31= 0; p32= 0; p33= 0; p34= 0; p35= 0; p36= 0


        action_flag = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12,p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36]

        action_str = ['action1', 'action2', 'action3', 'action4', 'action5', 'action6', 'action7', 'action8', 'action9', 'action10', 'action11', 'action12','action13', 'action14', 'action15', 'action16',\
               'action17', 'action18', 'action19', 'action20', 'action21', 'action22', 'action23', 'action24','action25', 'action26', 'action27', 'action28', 'action29', 'action30', 'action31', 'action32', 'action33', 'action34', 'action35', 'action36']

        rated_actions = []

#count the members of the array; to know how often they repeat
#for pm in range(0, len(par_mutate)):
        array_new = []

        for i in range(0, len(par_values)):
            check_once = 0
            for j in range(0, len(rates_var)):
                if par_values[i] == rates_var[j] and action_flag[j] == 0 and check_once == 0:
                    check_once = 1
                    action_flag[j] = 1
                    rated_actions.append(action_str[j])


        print('par_values')
        print(par_values)
        print('rates_var')
        print(rates_var)
        print('action_str')
        print(action_str)
        print('rated_actions')
        print(rated_actions)
#Except the 'GST-all' action and actions with the word 'child' in their name all actions that contain 'GST-' in their
#names will be collected into the 'expressio_list' array and used during the GA computation
        expression_list = []
        for i, action in enumerate(bpy.data.actions):
            if action.name.startswith("GST-") and "child" not in action.name and "GST-all" not in action.name:
                expression_list.append(action)
        print (expression_list)


##############################################################################################################################################
# The block below copies a parent action (into 'copied_gesture'). So the first children generated at the children panel will be the parents
# then the during subsequent computation the children will be copied into the children storage panel in the UI.
##############################################################################################################################################

        for i in range(0, len(expression_list)):
            copied_gesture =  expression_list[i].copy()

    ### counts the the number of gestures with character 'child' in their name. This count helps in determining the generation number of a child gesture ###
            count = 0
            for child_gesture in bpy.data.actions:
                if "child" in child_gesture.name:
                    count += 1

            if count == 0 or count <= 33:
                copied_gesture.name = "GST-child-" + expression_list[i].name[4:] + " " +  str(1)

            if count > 33:
                gen_num = int(count/33)+1
                copied_gesture.name = "GST-child-" + expression_list[i].name[4:] + " " +  str(gen_num)
######################################################################################################################

#Here save the set of actions to be bred/crossed-over and/or to be mutated in to the arrays 'expression_rated_array' and 'action_mutate' respectively.

        expression_rated_array = []
        action_mutate = []

        for i in range(0, len(action_str)):
            check_var = 0
            for act in range(0, len(rated_actions)):
                exp = expression_list[i]
                if rated_actions[act] == action_str[i]:
                    check_var += 1
                    if check_var == 1:
                        expression_rated_array.append(exp)
                        check_var = 2
            if check_var == 0:
                action_mutate.append(exp)

        print ('List of actions to be cross-overed')
        print (expression_rated_array)

        print('List of actions to be mutated')
        print(action_mutate)



##################################################################
                 ### Mutation Algorithm ###
##################################################################

#################################################################################################################################################
#mutation function; we mutate actions that are rated lowest(with value 0) by the user.
# In genetic algorithm the mutation rate is adviced to be very small. Heeding to this idea,here, mutation level
# of an action which is provided for mutation(an action rated 0 by the user) is kept to as low as in average to 1/8 of the total fcurves of
# the give action; assuming that random number generator has equal distribuion.
# Besides to reduce an exaggerated effect of mutation on the selected fcurves, their keyframes' mutation are limited to random values b/n 0 and 0.02. If the mutated actions tend to be very small then you can increase mutation by narrowing the random number range in 'random_num' and also you can start increasing random range of 'val' and see the effects.
#################################################################################################################################################

        a = 0
        while a < len(action_mutate):

            for i in range(0, len(action_mutate[a].fcurves.items())):
                random_num = random.randint(1,8)
                control_points = len(action_mutate[a].fcurves[i].keyframe_points.items())
                ii = 0
                while ii < control_points:
                    if random_num == 2:
                        val = random.uniform(0, 0.02)
                        keyframe = action_mutate[a].fcurves[i].keyframe_points[ii].co[1] = val
                        mutated_keyframes = action_mutate[a].fcurves[i].keyframe_points[ii].co
                #print ('mutated_keyframes')
                #print (action_mutate[a].fcurves[i].group.name)
                        ii += 1
                print (action_mutate[a])
                a += 1


        head_fcurves = ['pose.bones["head"].location', 'pose.bones["head-target"].location', 'pose.bones["head"].rotation_euler', 'pose.bones["DEF-neck"].rotation_euler'] 
        mouth_fcurves = ['pose.bones["mouth_D_L"].location', 'pose.bones["mouth_D_R"].location', 'pose.bones["mouth_U_L"].location', 'pose.bones["mouth_U_R"].location', 'pose.bones["mouth_C_R"].location', 'pose.bones["mouth_C_L"].location', 'pose.bones["lip_C_L"].location', 'pose.bones["lip_D"].location', 'pose.bones["lip_D_L"].location', 'pose.bones["lip_D_R"].location', 'pose.bones["lip_U_L"].location', 'pose.bones["chin"].location', 'pose.bones["lip_U"].location', 'pose.bones["lip_U_R"].location']
        eyes_fcurves = ['pose.bones["brow.C"].location', 'pose.bones["brow.R"].location', 'pose.bones["brow.L"].location', 'pose.bones["brow.inner.R"].location', 'pose.bones["eye.offset"].location', 'pose.bones["brow.inner.L"].location']
        head_eyes_fcurves = ['pose.bones["head"].location', 'pose.bones["head-target"].location', 'pose.bones["head"].rotation_euler', 'pose.bones["brow.C"].location', 'pose.bones["brow.R"].location', 'pose.bones["brow.L"].location', 'pose.bones["brow.inner.R"].location', 'pose.bones["eye.offset"].location', 'pose.bones["brow.inner.L"].location']
        head_mouth_fcurves = ['pose.bones["head"].location', 'pose.bones["head-target"].location', 'pose.bones["head"].rotation_euler', 'pose.bones["mouth_D_L"].location', 'pose.bones["mouth_D_R"].location', 'pose.bones["mouth_U_L"].location', 'pose.bones["mouth_U_R"].location', 'pose.bones["mouth_C_R"].location', 'pose.bones["mouth_C_L"].location', 'pose.bones["lip_C_L"].location', 'pose.bones["lip_D"].location', 'pose.bones["lip_D_L"].location', 'pose.bones["lip_D_R"].location', 'pose.bones["lip_U_L"].location', 'pose.bones["chin"].location', 'pose.bones["lip_U"].location', 'pose.bones["lip_U_R"].location']
        mouth_eyes_fcurves = ['pose.bones["mouth_D_L"].location', 'pose.bones["mouth_D_R"].location', 'pose.bones["mouth_U_L"].location', 'pose.bones["mouth_U_R"].location', 'pose.bones["mouth_C_R"].location', 'pose.bones["mouth_C_L"].location', 'pose.bones["lip_C_L"].location', 'pose.bones["lip_D"].location', 'pose.bones["lip_D_L"].location', 'pose.bones["lip_D_R"].location', 'pose.bones["lip_U_L"].location', 'pose.bones["chin"].location', 'pose.bones["lip_U"].location', 'pose.bones["lip_U_R"].location','pose.bones["brow.C"].location', 'pose.bones["brow.R"].location', 'pose.bones["brow.L"].location', 'pose.bones["brow.inner.R"].location', 'pose.bones["eye.offset"].location', 'pose.bones["brow.inner.L"].location']


#cross over function
        a = 0
        action_counter = -1
        while a < len(rated_actions)-1:
            action_counter += 1
            print (expression_rated_array[a])
            print (expression_rated_array[a+1])


#############################################################
###Algorithm for the cut and splice breeding technique###
##############################################################

            cut_splice = bpy.data.scenes['Scene'].cut_splice_var 
            if cut_splice == '1':        
                cut_and_splice_breeding_style = 1
            if cut_splice == '2':        
                cut_and_splice_breeding_style = 2
            if cut_splice == '3':        
                cut_and_splice_breeding_style = 3
            if cut_splice == '4':        
                cut_and_splice_breeding_style = 4
            if cut_splice == '5':        
                cut_and_splice_breeding_style = 5
            if cut_splice == '6':        
                cut_and_splice_breeding_style = 6
# Create (by copying) a child_action which is  a replica/copy of parent 1
# Then it removes the head part related fcurves from the child_action but leaves eyes and mouth related fcurves as they are
# And it copies the head related fcurves from parent 2 to child_action

            fcurves_to_be_removed = []
            fcurves_to_be_inserted = []

# Single group of fcurves (head, eyes or mouth) removal from the first parent 'cut and splice' breeding technique style
            if cut_and_splice_breeding_style == 1:
                fcurves_to_be_removed = head_fcurves
            if cut_and_splice_breeding_style == 2:
                fcurves_to_be_removed = eyes_fcurves
            if cut_and_splice_breeding_style == 3:
                fcurves_to_be_removed = mouth_fcurves
#Two group of fcurves(such as head and eyes, head and mouth, eyes and mouth etc.) removal from the first parent 'cut and splice' breeding technique style
            if cut_and_splice_breeding_style == 4:
                fcurves_to_be_removed = head_eyes_fcurves

           if cut_and_splice_breeding_style == 5:
               fcurves_to_be_removed = head_mouth_fcurves

           if cut_and_splice_breeding_style == 6:
               fcurves_to_be_removed = mouth_eyes_fcurves


 # remember here we can insert the capability to integrate which part of face's part is selected in the checkbox
            print('len(child_action.fcurves.items()_before removal)')
            print(expression_rated_array[a].name)
            print(len(expression_rated_array[a].fcurves.items()))
            print("len of curves_to_be_removed")
            print(fcurves_to_be_removed)
            fr  = []
            fr = fcurves_to_be_removed
# Subtract '2' from the total curves of the the reason is the start of the fcurves index is -1 for the action (bpy.data.actions['name'].fcurves[-1].data_path)
            max_fcurve_size = len(expression_rated_array[a].fcurves.items())-1 

            while max_fcurve_size >= 0:
                fcur = 0
                flag = 0 

                while fcur < len(fr) and flag == 0:
                    if expression_rated_array[a].fcurves[max_fcurve_size].data_path == fcurves_to_be_removed[fcur]:

                        expression_rated_array[a].fcurves.remove(expression_rated_array[a].fcurves[max_fcurve_size])
                        flag = 1
                        print("removed")
                    fcur += 1
                max_fcurve_size -= 1
        
            print('len(child_action.fcurves.items()_after removal)')
            print(expression_rated_array[a].name)
            print(len(expression_rated_array[a].fcurves.items()))
    

#copy head related fcurves from the 2nd parent to the child

   # selectedObj.animation_data.action = bpy.data.actions.new(name="GST-random1")
    #curve = selectedObj.animation_data.action.fcurves
            curve = expression_rated_array[a].fcurves

#just for naming convienance copy the values of the fcurves_to_be_removed to a new variable, it wouldn't make a d/ce at all to use fcurves_to_be_removed though
            fcurves_to_be_inserted = fcurves_to_be_removed

#Making the array of fcurves an outer loop help us in detecting an array of fcurves in the 2nd parent that can have the same data_path name
            for fcurves in range(0, len(fcurves_to_be_inserted)):
                duplicate_curve_name = 0
                for exp_fcurves in range(0, len(expression_rated_array[a+1].fcurves.items())):
                    if expression_rated_array[a+1].fcurves[exp_fcurves].data_path == fcurves_to_be_inserted[fcurves] and duplicate_curve_name == 0:
                        exp_fcurve_datapath = expression_rated_array[a+1].fcurves[exp_fcurves].data_path
                        exp_fcurve_index = expression_rated_array[a+1].fcurves[exp_fcurves].array_index
                 # Some fcurves are not assinged a group name, leaving it out is better, it generates errors during cross-over computation
                        #exp_fcurve_groupname = expression_rated_array[a+1].fcurves[exp_fcurves].group.name

              #creates a curve that have similar parameters to that of 2nd parent's head related fcurves
                        created_fcurve = curve.new(data_path = exp_fcurve_datapath, index = exp_fcurve_index)#, action_group = exp_fcurve_groupname)

          # counts the number of keyframe points in the specific head related fcurve of the 2nd parent
                        keyframe_count = len(expression_rated_array[a+1].fcurves[exp_fcurves].keyframe_points.items())

         # adds keyframe points, sized in number, equal to the retrieved count of keyframe points of the fcurve in the 2nd parent
                        created_fcurve.keyframe_points.add(keyframe_count)
                        duplicate_curve_name = 1

                        i = 0
                        while i < keyframe_count:
                            keypoint_co = expression_rated_array[a+1].fcurves[exp_fcurves].keyframe_points[i].co[0]
                            keyval_co = expression_rated_array[a+1].fcurves[exp_fcurves].keyframe_points[i].co[1]
                            created_fcurve.keyframe_points[i].co = keypoint_co, keyval_co
                            print("copied_fcurve_keyframe_points")
                            print(created_fcurve.keyframe_points[i].co)
                            i=i+1
            a += 1









