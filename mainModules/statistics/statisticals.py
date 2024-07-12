
#################################################################################################################
##############################################################################################################################################  Dict from TBL1 : FieldToolUser_Table
#Dictionary for Statistics of Summary/Graphs Page
def PatientStatisticsDictTbl1():

    #Retrieve a list of patients in the patient table
    userlist=[]
    for users in Patient_Profiles.objects.all():
        userlist.append(users.username)

    #Create dict to store statistics
    usercount={}
    for user in userlist:
        diaglist=[]
        for diag in Patient_Visits.objects.all():
            diaglist.append(diag.abbrev)

        #Get unique list of diagnosis from the visits table
        diaglist=set(diaglist)
              

        diagcount={}
        for diag in diaglist:
            diagcount[diag]=Patient_Visits.objects.filter(patientid=user, diagnosisid=diag).count()
        
        #Append items to dictionary
        usercount[user]={"diagnosis":diagcount}
	
      
        usercount[user]["filetypecount"]=filetypecount
        #print (filetypes)
    return usercount



##################################################################################################################################################

# VIEW STATISTICS
class ViewStatsAPI(MethodView):

    decorators = [auth_required]

    def get(self):
        category=categoryfind()
        
        return render_template("statistics.html",category=category)

class ViewStatsv2API(MethodView):

    decorators = [auth_required]

    def get(self):
        category=categoryfind()
        
        diaglist=[]
        for diag in diagnosiss_Tables.objects.all():
            diaglist.append(diag.abbrev)
              
        topiclist=[]
        for topic in TopicTable.objects.all():
            topiclist.append(topic.names)
            
        categorylist=[]
        for category in CategoryTable.objects.all():
            categorylist.append(category.names)
        
        sourcelist=["Schools","Media","Publisher","Community"]
        filetypelist=[]
        for filetypes in FieldCollections.objects.all():
            filetypelist.append(filetypes.typeoffile)
        filetype=[]
        for filetypeitems in filetypelist:
            if filetypeitems not in filetype:
                filetype.append(filetypeitems)
        
        return render_template("statistics.html",category=category, diaglist=diaglist, categorylist=categorylist, topiclist=topiclist, sourcelist=sourcelist, filetypelist=filetype, FieldCollections=FieldCollections, FieldToolUser_Table=FieldToolUser_Table)


#########################################################################################################################################################################################################################################################################################
##########################################################################################################################################
#MATPLOTLIB GRAPHING #
def UserStatisticsDict():
    userlist=[]
    for users in FieldToolUser_Table.objects.all():
        userlist.append(users.username)
    usercount={}
    for user in userlist:
        langlist=[]
        for lang in Languages_Tables.objects.all():
            langlist.append(lang.abbrev)
              
        topiclist=[]
        for topic in TopicTable.objects.all():
            topiclist.append(topic.names)
            
        categorylist=[]
        for category in CategoryTable.objects.all():
            categorylist.append(category.names)
        
        sourcelist=["Schools","Media","Publisher","Community"]
        for source in FieldCollections.objects.all():
            sourcelist.append(source.source)
        sources=[]
        for sourceitems in sourcelist:
            if  sourceitems not in sources:
                sources.append(sourceitems)
        
        langcount={}
        for lang in langlist:
            langcount[lang]=FieldCollections.objects.filter(researchassisstantid=user, languageid=lang).count()
        
        topiccount={}       
        for topic in topiclist:
        	topiccount[topic]=FieldCollections.objects(researchassisstantid=user, topicid=topic).count()
        
        sourcecount={}
        for source in sources:
            sourcecount[source]=FieldCollections.objects.filter(researchassisstantid=user, source=source).count()
        
        categorycount={}
        for category in categorylist:
            categorycount[category]=FieldCollections.objects.filter(researchassisstantid=user, categoryid=category).count()
        usercount[user]={"languages":langcount,"topics":topiccount,"sources": sourcecount,"category":categorycount}
	#        return json.dumps(usercount)
        metadatalist=[]
        for metadata in FieldCollections.objects.filter(researchassisstantid=user):
            metadatalist.append(metadata.metadataid)
            
        filetypes=["audio", "images", "text", "others"]

        filetypecount={}
        for files in filetypes:
            filetypecount[files]=0
        for metadata in metadatalist:
            for typefile in FileUnit.objects.filter(metadataid=metadata):
                file_type=typefile.typeoffile
                filetypecount[file_type] =filetypecount[file_type]+1
        usercount[user]["filetypecount"]=filetypecount
        #print (filetypes)
    return usercount






###########################################################################################################################################
totaldict= UserStatisticsDict()   
#print (totaldict)
def diagimage():
        X=[]
        for user in totaldict:
            X.append(user)

        attrdict={}

#for user in userlist:
        keylist=[]

        for key in totaldict[user]["diagnosiss"]:
        	attrdict[key]=[]
        	for user in X:
                    attrdict[key].append(totaldict[user]["diagnosiss"][key])                                      
#for key in attrdict: 
#	exec(key=attrdict[key])
	

        #print (attrdict)
        MEDIC=attrdict["MEDIC"]
        LAB=attrdict["LAB"]
        COMPLAINT=attrdict["COMPLAINT"]
        SYMPTOM=attrdict["SYMPTOM"]
        DIAGNOSIS=attrdict["DIAGNOSIS"]



        X_axis=np.arange(len(X))
        width=0.2 
        plt.bar(X_axis, MEDIC, width=width,label="MEDIC")
        plt.bar(X_axis+width, LAB, width=width,label="LAB")
        plt.bar(X_axis+width*2, COMPLAINT, width=width,label="COMPLAINT")
        plt.bar(X_axis+width*3, SYMPTOM, width=width,label="SYMPTOM")
        plt.bar(X_axis+width*4, DIAGNOSIS, width=width,label="DIAGNOSIS")

        plt.xticks(X_axis,X)

        plt.legend()
        plt.show()


        #image to template
        from io import BytesIO

        diagimage = BytesIO()
        plt.savefig(diagimage, format='png')
        import base64
        diagimage_png = base64.b64encode(diagimage.getbuffer()).decode("ascii")
        return diagimage_png




######################################################################################################################################
##########################PIE CHARTS
#diagnosis PIE
def diag_pie():
        diaglist=[]
        for diagnosis in diagnosiss_Tables.objects.all():
            diaglist.append(diagnosis.abbrev)

        total_list=[]
        for diagnosiss in diaglist:
            total_list.append(FieldCollections.objects.filter(diagnosisid=diagnosiss).count())

        y = np.array(total_list)

        plt.pie(y, labels=diaglist)
        plt.legend()
        plt.show()

        from io import BytesIO
        piediagimage = BytesIO()
        plt.savefig(piediagimage, format='png')

        import base64
        piediag_png = base64.b64encode(piediagimage.getbuffer()).decode("ascii")
        return piediag_png  


#######################################################################################################################################
####################WEBPAGE PLOTS : bars and pies

# diagnosis Bar
class ViewGraphdiagAPI(MethodView):
    def get(self):
        piediag=diag_pie()
        plt.clf()
        diagimage_png = diagimage()
        plt.clf()
        return render_template("stats.html", message=diagimage_png, msg="diagnosis Statistics per User",message1=piediag, msg1="diagnosiss Pie Chart")

