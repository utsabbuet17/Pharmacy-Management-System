from tkinter import *
import sys
from tkinter import messagebox



top  = Tk()

top.geometry('1140x750+0+0')
top.title('LOGIN SCREEN')
top.configure(background = 'White')

global entry1_2
global entry2_2



global medecine_list
medecine_list = ['napa', ' 2 ', '10', 'Fever', 'metryl', ' 5 ', '50', ' Dysentery ', 'azith', ' 10 ', '30',
                     'Antibiotic']


#============== Function for login as general Member ========================
def log_gen():
    # global top_1
    #
    #
    up = Label(top, bg='#6fa1f8', padx=750, pady=700)
    up.pack()
    up.place(x=400, y=150)

    # ======================== function for searching medicine ===================


    def page_2():


        x = str(entry1_3.get())


        if len(x) == 11:
            #global top_1

            top_1 = Toplevel()

            top_1.geometry('1140x750+0+0')
            top_1.title('Search Medicine')
            top_1.configure(background='White')


            def search():

                get_med = str(medicine.get())
                get_med = get_med.lower()
                for i in range(0,len(medecine_list)):
                    if get_med == medecine_list[i]:
                        medicine_name.insert(0,medecine_list[i].upper( ))
                        ppu_value.insert(0, medecine_list[i+1])
                        tot_am.insert(0, medecine_list[i + 2])
                        treat_for.insert(0, medecine_list[i+3])




            # top_1.geometry('1140x750+0+0')
            # top_1.title('Search Medicine')
            # top_1.configure(background='White')

            up = Label(top_1, bg='green', padx=750, pady=700)
            up.pack()
            up.place(x=0, y=150)


            lbl_3 = Label(top_1, text='Welcome as General Member', fg='green')
            lbl_3.config(font=('Arial', 39, 'bold'))
            lbl_3.pack()


            global medicine

            medicine = Entry(top_1, width=30)
            medicine.pack(pady=10)
            medicine.config(font=('Arial',15))
            medicine.place(x=350, y=80)

            search = Button(top_1, text='Search for Medicine', font=('Helvetica', 12), bg ='#856ff8', command = search)
            search.pack()
            search.place(x=720, y=80)

            name = Label(top_1, text='Name:', font=("Times", 15))
            name.pack()
            name.place(x=50, y=200)

            global medicine_name

            medicine_name = Entry(top_1, width=20)
            medicine_name.pack()
            medicine_name.config(font=('Arial',15))
            medicine_name.place(x=116, y=200)

            ppu = Label(top_1, text='Price Per Unit:', font=("Times", 15))
            ppu.pack()
            ppu.place(x=50, y=250)

            global ppu_value

            ppu_value = Entry(top_1, width=20)
            ppu_value.pack()
            ppu_value.config(font=('Arial', 15))
            ppu_value.place(x=181, y=250)

            treat = Label(top_1, text='Used For:', font=("Times", 15))
            treat.pack()
            treat.place(x=50, y=300)

            global treat_for

            treat_for = Entry(top_1, width=20)
            treat_for.config(font=('Arial', 15))

            treat_for.pack()
            treat_for.place(x=142, y=300)

            count = Label(top_1, text='Total Amount:', font=("Times", 15))
            count.pack()
            count.place(x=50, y=350)

            global tot_am

            tot_am = Entry(top_1, width=20)
            tot_am.config(font=('Arial', 15))

            tot_am.pack()
            tot_am.place(x=179, y=350)


            top_1.mainloop()

        else:
            messagebox.showwarning("Warning", "The number is not valid")


    def cancel():
        top.destroy()
        sys.exit()

    lbl1_3 = Label(top, text='Phone Number*: ', font=('Helvetica', 17),bg = '#b0d108')
    lbl1_3.pack()
    lbl1_3.place(x=620, y=150)


    global entry1_3
    entry1_3 = Entry(top, width = 50)
    entry1_3.config(font=('Arial',12))
    entry1_3.pack()
    entry1_3.place(x=510, y=190)


    button3_3 = Button(top, text='Cancel', font=('Helvetica', 14), bg ='red', command=cancel)
    button3_3.pack()
    button3_3.place(x=890, y=220)

    button4_3 = Button(top, text='Enter', font=('Helvetica', 14), bg ='green', command=page_2)
    button4_3.pack()
    button4_3.place(x=510, y=220)

#============== Function for login as Worker ========================

def log_work():
    up = Label(top, bg='#6fa1f8', padx=750, pady=700)
    up.pack()
    up.place(x=400, y=150)





    def page_3():
        x = str(entry1_2.get())
        y = str(entry2_2.get())
        if len(x) == 0 and len(y) == 0:
            messagebox.showwarning("Warning", "Invalid ID Or Password")


        else:
            root = Tk()
            root.geometry('1140x750+0+0')
            root.title('Main Page')

            #total_sale = StringVar()

            up = Label(root, bg='green', padx=750, pady=700)
            up.pack()
            up.place(x=0, y=130)

            def show(x, y):
                if x == '0' and y == '0':
                    return 'None'
                elif x == '0':
                    return 'Female'
                elif y == '0':
                    return 'Male'
                else:
                    return 'You Have Selected Both'

            def add_medicine_list(name, perUnit, totalUnit, used):
                medecine_list.append(name.lower())
                medecine_list.append(perUnit)
                medecine_list.append(totalUnit)
                medecine_list.append(used)

                messagebox.showinfo('Confirmation', 'List is Updated')

            def search_for_medi(x):
                if x != 'Write Here':

                    A = Label(root, text="Medicine Name", bg='#d6a41a')
                    A.config(font=('Arial', 15, 'bold'))
                    A.pack()
                    A.place(x=50, y=400)
                    Name = Entry(root, width=20, justify='center')
                    Name.pack()
                    Name.place(x=210, y=400)
                    Name.config(font=('Arial', 14, 'bold'))

                    A = Label(root, text="Per Unit Price", bg='#d6a41a')
                    A.config(font=('Arial', 15, 'bold'))
                    A.pack()
                    A.place(x=50, y=450)
                    per_unit = Entry(root, width=20, justify='center')
                    per_unit.pack()
                    per_unit.place(x=210, y=450)
                    per_unit.config(font=('Arial', 14, 'bold'))

                    A = Label(root, text="Total Unit", bg='#d6a41a')
                    A.config(font=('Arial', 15, 'bold'))
                    A.pack()
                    A.place(x=50, y=500)
                    total_u = Entry(root, width=20, justify='center')
                    total_u.pack()
                    total_u.place(x=210, y=500)
                    total_u.config(font=('Arial', 14, 'bold'))

                    A = Label(root, text="Used For", bg='#d6a41a')
                    A.config(font=('Arial', 15, 'bold'))
                    A.pack()
                    A.place(x=50, y=550)
                    used_for = Entry(root, width=20, justify='center')
                    used_for.pack()
                    used_for.place(x=210, y=550)
                    used_for.config(font=('Arial', 14, 'bold'))

                    for i in range(0, len(medecine_list)):
                        if x.lower() == medecine_list[i]:
                            Name.insert(0, medecine_list[i].upper())
                            per_unit.insert(0, medecine_list[i + 1])
                            total_u.insert(0, medecine_list[i + 2])
                            used_for.insert(0, medecine_list[i + 3])




                else:

                    sec_1 = Label(root, bg='#d6a41a', padx=270, pady=500)
                    sec_1.pack()
                    sec_1.place(x=20, y=400)

                    A = Label(root, text="PLEASE ENTER A NAME", bg='#d6a41a')
                    A.config(font=('Arial', 15, 'bold'))
                    A.pack()
                    A.place(x=160, y=500)

            def appointment(name, age, male, female, village, upozila, district, description, date, phone):
                gender = show(male, female)
                print(name, age, gender, village, upozila, district, description, date, phone)

                f = open('App\ ' + name + ".txt", "w")
                f.write("Name " + name + "\n")
                f.write(
                    "Age " + age + "\n" + "Gender " + gender + "\n" + "Village " + village + "\n" + "Upozila " + upozila + "\n" + "District " + district + "\n" + "Description " + description + "\n" + "Date & Time " + date + "\n" + "Phone NO. " + phone + "\n")
                f.close()

            def sales_function(recipt_no, name, age, male, female, address, medi_1, ppu_1, tu_1, medi_2, ppu_2, tu_2,
                               medi_3, ppu_3,
                               tu_3, medi_4, ppu_4, tu_4, medi_5, ppu_5, tu_5, medi_6, ppu_6, tu_6,
                               medi_7, ppu_7, tu_7, medi_8, ppu_8, tu_8, medi_9, ppu_9, tu_9):
                gender = show(male, female)
                f = open('Sales\ ' + name + '__' + recipt_no + ".txt", "w")
                f.write("Name " + name + "\n")
                f.write(
                    "Recipt NO." + recipt_no + "\n\n" + "Name " + name + "\n\n" + "Age " + age + "\n" + "Gender " + gender + "\n" + "Address " + address + "\n" + "Medicine_1 " + medi_1 + "\t" + "Per Unit Price " + ppu_1 + "\t" + "Total Unit " + tu_1 + "\n" + "Medicine_2 " + medi_2 + "\t" + "Per Unit Price " + ppu_2 + "\t" + "Total Unit " + tu_2 + "\n" + "Medicine_3 " + medi_3 + "\t" + "Per Unit Price " + ppu_3 + "\t" + "Total Unit " + tu_3 + "\n" + "Medicine_4 " + medi_4 + "\t" + "Per Unit Price " + ppu_4 + "\t" + "Total Unit " + tu_4 + "\n" + "Medicine_5 " + medi_5 + "\t" + "Per Unit Price " + ppu_5 + "\t" + "Total Unit " + tu_5 + "\n" + "Medicine_6 " + medi_6 + "\t" + "Per Unit Price " + ppu_6 + "\t" + "Total Unit " + tu_6 + "\n" + "Medicine_7 " + medi_7 + "\t" + "Per Unit Price " + ppu_7 + "\t" + "Total Unit " + tu_7 + "\n" + "Medicine_1 " + medi_8 + "\t" + "Per Unit Price " + ppu_8 + "\t" + "Total Unit " + tu_8 + "\n" + "Medicine_9 " + medi_9 + "\t" + "Per Unit Price " + ppu_9 + "\t" + "Total Unit " + tu_9 + "\n\n")
                f.close()
                global total
                total = float(ppu_1) * float(
                    tu_1) + float(ppu_2) * float(tu_2) + float(ppu_3) * float(tu_3) + float(ppu_4) * float(
                    tu_4) + float(
                    ppu_5) * float(tu_5) + float(ppu_6) * float(tu_6) + float(ppu_7) * float(tu_7) + float(
                    ppu_8) * float(
                    tu_8) + float(ppu_9) * float(tu_9)
                #total_sale.set(total)
                totall.delete(0,END)
                totall.insert(0,total)

            ###########################################################################################
            #################### Pages ################################################################
            def sales_f():
                up = Label(root, bg='green', padx=750, pady=700)
                up.pack()
                up.place(x=0, y=200)

                n = Label(root, text='Name of Patient: ', bg='green')
                n.config(font=('Arial', 12, 'bold'))
                n.pack()
                n.place(x=20, y=220)

                name = Entry(root, width=30)
                name.pack()
                name.place(x=155, y=225)

                a = Label(root, text='Age: ', bg='green')
                a.config(font=('Arial', 12, 'bold'))
                a.pack()
                a.place(x=430, y=220)

                age = Entry(root, width=10)
                age.pack()
                age.place(x=480, y=225)

                var_male = StringVar()
                male = Checkbutton(root, text='Male', bg='green', variable=var_male, onvalue='Male', offvalue='0')
                male.config(font=('Arial', 12, 'bold'))
                male.select()
                male.pack()
                male.place(x=650, y=220)

                var_female = StringVar()
                female = Checkbutton(root, text='Female', bg='green', variable=var_female, onvalue='female',
                                     offvalue='0')
                female.config(font=('Arial', 12, 'bold'))
                female.deselect()
                female.pack()
                female.place(x=750, y=220)

                ad = Label(root, text='Address: ', bg='green')
                ad.pack()
                ad.config(font=('Arial', 12, 'bold'))
                ad.place(x=20, y=280)

                add_text = StringVar(root, value='Not selected')
                address = Entry(root, width=100, textvariable=add_text)
                address.pack()
                address.place(x=120, y=285)

                # ===============  Medicine List  ==================================================
                m = Label(root, text="Medicine 1: ", bg='#3ea8e6')
                m.pack()
                m.place(x=20, y=360)
                m_1 = Entry(root, width=40)
                m_1.pack()
                m_1.place(x=120, y=360)

                m = Label(root, text='P. U.Price :', bg='#3ea8e6')
                m.pack()
                m.place(x=400, y=360)
                pup_1 = Entry(root, width=9)
                pup_1.pack()
                pup_1.place(x=480, y=360)

                m = Label(root, text='No. of Unit :', bg='#3ea8e6')
                m.pack()
                m.place(x=580, y=360)
                tu_1 = Entry(root, width=9)
                tu_1.pack()
                tu_1.place(x=670, y=360)
                # ====================================================================
                m = Label(root, text="Medicine 2: ", bg='#3ea8e6')
                m.pack()
                m.place(x=20, y=400)
                m2 = StringVar(root, value='None')
                m_2 = Entry(root, width=40, textvariable=m2)
                m_2.pack()
                m_2.place(x=120, y=400)

                m = Label(root, text='P. U.Price :', bg='#3ea8e6')
                m.pack()
                m.place(x=400, y=400)
                p2 = IntVar(root, value=0)
                pup_2 = Entry(root, width=9, textvariable=p2)
                pup_2.pack()
                pup_2.place(x=480, y=400)

                m = Label(root, text='No. of Unit :', bg='#3ea8e6')
                m.pack()
                m.place(x=580, y=400)
                t2 = IntVar(root, value=0)
                tu_2 = Entry(root, width=9, textvariable=t2)
                tu_2.pack()
                tu_2.place(x=670, y=400)
                # ========================================================================

                m = Label(root, text="Medicine 3: ", bg='#3ea8e6')
                m.pack()
                m.place(x=20, y=440)
                m3 = StringVar(root, value='None')
                m_3 = Entry(root, width=40, textvariable=m3)
                m_3.pack()
                m_3.place(x=120, y=440)

                m = Label(root, text='P. U.Price :', bg='#3ea8e6')
                m.pack()
                m.place(x=400, y=440)
                p3 = IntVar(root, value=0)
                pup_3 = Entry(root, width=9, textvariable=p3)
                pup_3.pack()
                pup_3.place(x=480, y=440)

                m = Label(root, text='No. of Unit :', bg='#3ea8e6')
                m.pack()
                m.place(x=580, y=440)
                t3 = IntVar(root, value=0)
                tu_3 = Entry(root, width=9, textvariable=t3)
                tu_3.pack()
                tu_3.place(x=670, y=440)
                # ========================================================================

                m = Label(root, text="Medicine 4: ", bg='#3ea8e6')
                m.pack()
                m.place(x=20, y=480)
                m4 = StringVar(root, value='None')
                m_4 = Entry(root, width=40, textvariable=m4)
                m_4.pack()
                m_4.place(x=120, y=480)

                m = Label(root, text='P. U.Price :', bg='#3ea8e6')
                m.pack()
                m.place(x=400, y=480)
                p4 = IntVar(root, value=0)
                pup_4 = Entry(root, width=9, textvariable=p4)
                pup_4.pack()
                pup_4.place(x=480, y=480)

                m = Label(root, text='No. of Unit :', bg='#3ea8e6')
                m.pack()
                m.place(x=580, y=480)
                t4 = IntVar(root, value=0)
                tu_4 = Entry(root, width=9, textvariable=t4)
                tu_4.pack()
                tu_4.place(x=670, y=480)
                # ========================================================================

                m = Label(root, text="Medicine 5: ", bg='#3ea8e6')
                m.pack()
                m.place(x=20, y=520)
                m5 = StringVar(root, value='None')
                m_5 = Entry(root, width=40, textvariable=m5)
                m_5.pack()
                m_5.place(x=120, y=520)

                m = Label(root, text='P. U.Price :', bg='#3ea8e6')
                m.pack()
                m.place(x=400, y=520)
                p5 = IntVar(root, value=0)
                pup_5 = Entry(root, width=9, textvariable=p5)
                pup_5.pack()
                pup_5.place(x=480, y=520)

                m = Label(root, text='No. of Unit :', bg='#3ea8e6')
                m.pack()
                m.place(x=580, y=520)
                t5 = IntVar(root, value=0)
                tu_5 = Entry(root, width=9, textvariable=t5)
                tu_5.pack()
                tu_5.place(x=670, y=520)
                # ========================================================================

                m = Label(root, text="Medicine 6: ", bg='#3ea8e6')
                m.pack()
                m.place(x=20, y=560)
                m6 = StringVar(root, value='None')
                m_6 = Entry(root, width=40, textvariable=m6)
                m_6.pack()
                m_6.place(x=120, y=560)

                m = Label(root, text='P. U.Price :', bg='#3ea8e6')
                m.pack()
                m.place(x=400, y=560)
                p6 = IntVar(root, value=0)
                pup_6 = Entry(root, width=9, textvariable=p6)
                pup_6.pack()
                pup_6.place(x=480, y=560)

                m = Label(root, text='No. of Unit :', bg='#3ea8e6')
                m.pack()
                m.place(x=580, y=560)
                t6 = IntVar(root, value=0)
                tu_6 = Entry(root, width=9, textvariable=t6)
                tu_6.pack()
                tu_6.place(x=670, y=560)
                # ========================================================================
                m = Label(root, text="Medicine 7: ", bg='#3ea8e6')
                m.pack()
                m.place(x=20, y=600)
                m7 = StringVar(root, value='None')
                m_7 = Entry(root, width=40, textvariable=m7)
                m_7.pack()
                m_7.place(x=120, y=600)

                m = Label(root, text='P. U.Price :', bg='#3ea8e6')
                m.pack()
                m.place(x=400, y=600)
                p7 = IntVar(root, value=0)
                pup_7 = Entry(root, width=9, textvariable=p7)
                pup_7.pack()
                pup_7.place(x=480, y=600)

                m = Label(root, text='No. of Unit :', bg='#3ea8e6')
                m.pack()
                m.place(x=580, y=600)
                t7 = IntVar(root, value=0)
                tu_7 = Entry(root, width=9, textvariable=t7)
                tu_7.pack()
                tu_7.place(x=670, y=600)
                # ========================================================================

                m = Label(root, text="Medicine 8: ", bg='#3ea8e6')
                m.pack()
                m.place(x=20, y=640)
                m8 = StringVar(root, value='None')
                m_8 = Entry(root, width=40, textvariable=m8)
                m_8.pack()
                m_8.place(x=120, y=640)

                m = Label(root, text='P. U.Price :', bg='#3ea8e6')
                m.pack()
                m.place(x=400, y=640)
                p8 = IntVar(root, value=0)
                pup_8 = Entry(root, width=9, textvariable=p8)
                pup_8.pack()
                pup_8.place(x=480, y=640)

                m = Label(root, text='No. of Unit :', bg='#3ea8e6')
                m.pack()
                m.place(x=580, y=640)
                t8 = IntVar(root, value=0)
                tu_8 = Entry(root, width=9, textvariable=t8)
                tu_8.pack()
                tu_8.place(x=670, y=640)
                # ========================================================================
                m9 = StringVar(root, value='None')
                m = Label(root, text="Medicine 9: ", bg='#3ea8e6')
                m.pack()
                m.place(x=20, y=680)
                m_9 = Entry(root, width=40, textvariable=m9)
                m_9.pack()
                m_9.place(x=120, y=680)

                m = Label(root, text='P. U.Price :', bg='#3ea8e6')
                m.pack()
                m.place(x=400, y=680)
                p9 = IntVar(root, value=0)
                pup_9 = Entry(root, width=9, textvariable=p9)
                pup_9.pack()
                pup_9.place(x=480, y=680)

                m = Label(root, text='No. of Unit :', bg='#3ea8e6')
                m.pack()
                m.place(x=580, y=680)
                t9 = IntVar(root, value=0)
                tu_9 = Entry(root, width=9, textvariable=t9)
                tu_9.pack()
                tu_9.place(x=670, y=680)
                # =============================== Medicine list end =========================================

                # ===============================Total cost==================================================

                tt = Label(root, text='TOTAL COST', bg='white')
                tt.config(font=('Arial', 30, 'bold'))
                tt.pack()
                tt.place(x=800, y=350)
                global totall
                to=IntVar(root, value=0)
                totall = Entry(root, width=10, textvariable=to)
                totall.config(font=('Arial', 28, 'bold'))
                totall.pack()
                totall.place(x=817, y=450)


                rc = Label(root, text='Recipt No.', bg='white')
                rc.config(font=('Arial', 10, 'bold'))
                rc.pack()
                rc.place(x=800, y=580)

                rc_n = Entry(root, width=10)
                rc_n.config(font=('Arial', 15, 'bold'))
                rc_n.pack()
                rc_n.place(x=800, y=610)

                # recipt_no, name, age, male, female, address, medi_1, ppu_1, tu_1, medi_2='None', ppu_2=0, tu_2=0,
                # medi_3='None', ppu_3=0,
                # tu_3=0, medi_4='None', ppu_4=0, tu_4=0, medi_5='None', ppu_5=0, tu_5=0, medi_6='None', ppu_6=0, tu_6=0,
                # medi_7='None', ppu_7=0, tu_7=0, medi_8='None', ppu_8=0, tu_8=0, medi_9='None', ppu_9=0, tu_9=0

                print_s = Button(root, text='Print', padx=60, pady=5,
                                 command=lambda: sales_function(rc_n.get(), name.get(), age.get(), var_male.get(),
                                                                var_female.get(),
                                                                address.get(), m_1.get(), pup_1.get(), tu_1.get(),
                                                                m_2.get(),
                                                                pup_2.get(),
                                                                tu_2.get(), m_3.get(), pup_3.get(), tu_3.get(),
                                                                m_4.get(),
                                                                pup_4.get(),
                                                                tu_4.get(), m_5.get(), pup_5.get(), tu_5.get(),
                                                                m_6.get(),
                                                                pup_6.get(),
                                                                tu_6.get(), m_7.get(), pup_7.get(), tu_7.get(),
                                                                m_8.get(),
                                                                pup_8.get(),
                                                                tu_8.get(), m_9.get(), pup_9.get(), tu_9.get()))
                print_s.pack()
                print_s.place(x=800, y=700)

                reset = Button(root, text='RESET', padx=40, pady=5, bg='red')
                reset.pack()
                reset.place(x=970, y=700)

            ######################################################################################################

            def app_f():
                up = Label(root, bg='green', padx=750, pady=700)
                up.pack()
                up.place(x=0, y=200)

                n = Label(root, text='Name of Patient: ', bg='green')
                n.config(font=('Arial', 12, 'bold'))
                n.pack()
                n.place(x=20, y=220)

                name = Entry(root, width=30)
                name.pack()
                name.place(x=155, y=225)

                a = Label(root, text='Age: ', bg='green')
                a.config(font=('Arial', 12, 'bold'))
                a.pack()
                a.place(x=430, y=220)

                age = Entry(root, width=10)
                age.pack()
                age.place(x=480, y=225)

                var_male = StringVar()
                male_a = Checkbutton(root, text='Male', bg='green', variable=var_male, onvalue='Male', offvalue='0')
                male_a.config(font=('Arial', 12, 'bold'))
                male_a.select()
                male_a.pack()
                male_a.place(x=650, y=220)

                var_female = StringVar()
                female = Checkbutton(root, text='Female', bg='green', variable=var_female, onvalue='female',
                                     offvalue='0')
                female.config(font=('Arial', 12, 'bold'))
                female.deselect()
                female.pack()
                female.place(x=750, y=220)

                ad = Label(root, text='Village: ', bg='green')
                ad.pack()
                ad.config(font=('Arial', 12, 'bold'))
                ad.place(x=20, y=280)

                vill_text = StringVar(root, value='Not selected')
                village = Entry(root, width=20, textvariable=vill_text)
                village.pack()
                village.place(x=110, y=285)

                ad = Label(root, text='Upozila: ', bg='green')
                ad.pack()
                ad.config(font=('Arial', 12, 'bold'))
                ad.place(x=350, y=280)

                up_text = StringVar(root, value='Not selected')
                upozila = Entry(root, width=20, textvariable=up_text)
                upozila.pack()
                upozila.place(x=440, y=285)

                D = Label(root, text='District: ', bg='green')
                D.pack()
                D.config(font=('Arial', 12, 'bold'))
                D.place(x=660, y=280)

                dis_text = StringVar(root, value='Not selected')
                district = Entry(root, width=20, textvariable=dis_text)
                district.pack()
                district.place(x=750, y=285)

                De = Label(root, text='Short Description of Problem: ', bg='green')
                De.config(font=('Arial', 12, 'bold'))
                De.pack()
                De.place(x=10, y=350)

                des = Text(root, height=8, width=40)
                des.pack()
                des.place(x=250, y=350)
                des.config(font=('Arial', 15, 'bold'))

                td = Label(root, text='Appointment Time & Date: ', bg='green', fg='red')
                td.pack()
                td.place(x=10, y=600)
                td.config(font=('Arial', 22, 'bold'))

                time_date = Entry(root)
                time_date.pack()
                time_date.place(x=400, y=605)
                time_date.config(font=('Arial', 22, 'bold'))

                ph = Label(root, text='Phone Number: ', bg='green')
                ph.pack()
                ph.place(x=750, y=405)
                ph.config(font=('Arial', 15, 'bold'))

                phone = Entry(root)
                phone.pack()
                phone.place(x=750, y=440)
                phone.config(font=('Arial', 17, 'bold'))
                # =====================================================

                print_a = Button(root, text='Confirm & Print', padx=25, pady=5,
                                 command=lambda: appointment(name.get(), age.get(), var_male.get(), var_female.get(),
                                                             village.get(),
                                                             upozila.get(), district.get(), des.get(1.0, END),
                                                             time_date.get(),
                                                             phone.get()))
                print_a.config(font=('Arial', 8, 'bold'))
                print_a.pack()
                print_a.place(x=800, y=700)

                reset = Button(root, text='RESET', padx=40, pady=5, bg='red')
                reset.pack()
                reset.place(x=970, y=700)

            ########################################################################################################
            ########################################################################################################
            def inv_f():
                up = Label(root, bg='green', padx=570, pady=700)
                up.pack()
                up.place(x=0, y=200)

                sec_1 = Label(root, bg='#d6a41a', padx=400, pady=700)
                sec_1.pack()
                sec_1.place(x=20, y=220)

                sec_2 = Label(root, bg='#69cf25', padx=270, pady=700)
                sec_2.pack()
                sec_2.place(x=580, y=220)
                # -------------------------------------------------------------------------------------------------
                SEARCH = Label(root, text="Search Section", bg='#d6a41a')
                SEARCH.pack()
                SEARCH.config(font=('Letter Craft', 35, 'bold'))
                SEARCH.place(x=120, y=220)

                A = Label(root, text="Search For Medicine", bg='#d6a41a')
                A.config(font=('Arial', 15, 'bold'))
                A.pack()
                A.place(x=160, y=300)
                txt_s = StringVar(root, value='Write Here')
                search_m = Entry(root, width=20, textvariable=txt_s)
                search_m.pack()
                search_m.place(x=150, y=350)
                search_m.config(font=('Arial', 14, 'bold'))

                search_medi = Button(root, text="SEARCH", bg='purple', padx=45, pady=5,
                                     command=lambda: search_for_medi(search_m.get()))
                search_medi.pack()
                search_medi.place(x=400, y=700)

                # --------------------------------------------------------------------------------------------------
                am = Label(root, text="Add New Medicine", bg='#69cf25')
                am.pack()
                am.config(font=('Letter Craft', 30, 'bold'))
                am.place(x=660, y=220)

                A = Label(root, text="Medicine Name", bg='#69cf25')
                A.config(font=('Arial', 15, 'bold'))
                A.pack()
                A.place(x=610, y=300)
                txt = StringVar(root, value='Null')
                add = Entry(root, width=20, textvariable=txt)
                add.pack()
                add.place(x=770, y=300)
                add.config(font=('Arial', 14, 'bold'))

                A = Label(root, text="Per Unit Price", bg='#69cf25')
                A.config(font=('Arial', 15, 'bold'))
                A.pack()
                A.place(x=610, y=370)
                txt_per = IntVar(root, value=0)
                per = Entry(root, width=20, textvariable=txt_per)
                per.pack()
                per.place(x=770, y=370)
                per.config(font=('Arial', 14, 'bold'))

                A = Label(root, text="Total Unit", bg='#69cf25')
                A.config(font=('Arial', 15, 'bold'))
                A.pack()
                A.place(x=610, y=430)
                txt_t = IntVar(root, value=0)
                total_unit = Entry(root, width=20, textvariable=txt_t)
                total_unit.pack()
                total_unit.place(x=770, y=430)
                total_unit.config(font=('Arial', 14, 'bold'))

                A = Label(root, text="Used For", bg='#69cf25')
                A.config(font=('Arial', 15, 'bold'))
                A.pack()
                A.place(x=610, y=500)
                txt_used = StringVar(root, value='Null')
                used = Entry(root, width=20, textvariable=txt_used)
                used.pack()
                used.place(x=770, y=500)
                used.config(font=('Arial', 14, 'bold'))

                add_medi = Button(root, text="ADD", bg='purple', padx=45, pady=5,
                                  command=lambda: add_medicine_list(add.get(), per.get(), total_unit.get(), used.get()))
                add_medi.pack()
                add_medi.place(x=820, y=700)

                reset = Button(root, text='RESET', padx=40, pady=5, bg='red')
                reset.pack()
                reset.place(x=970, y=700)

            #########################################################################################################
            #################################   MAIN PAGE   #########################################################
            #########################################################################################################

            l = Label(root, text="Welcome To Pharmacy Management System", fg='green')
            l.config(font=('Letter Craft', 39, 'bold'))
            l.pack()

            sales = Button(root, text='Sales', padx=110, pady=5, command=sales_f)
            sales.config(font=('Arial', 35, 'bold'))
            sales.pack()
            sales.place(x=0, y=100)

            app = Button(root, text='Appointment', padx=40, pady=5, command=app_f)
            app.config(font=('Arial', 35, 'bold'))
            app.pack()
            app.place(x=370, y=100)

            inv = Button(root, text='Inventory', padx=60, pady=5, command=inv_f)
            inv.config(font=('Arial', 35, 'bold'))
            inv.pack()
            inv.place(x=770, y=100)

            root.mainloop()









    def cancel():
        top.destroy()
        top.destroy()
        sys.exit()

    lbl1_2 = Label(top, text='Username*: ', font=('Helvetica', 17),bg = '#b0d108')
    lbl1_2.pack()
    lbl1_2.place(x= 640 , y = 160)


    entry1_2 = Entry(top, width = 50)
    entry1_2.config(font=('Arial', 12))
    entry1_2.pack()
    entry1_2.place(x=510, y=200)

    #
    lbl2_2 = Label(top, text ='Password*: ', font =('Helvetica', 17),bg = '#b0d108')
    lbl2_2.pack()
    lbl2_2.place(x= 640 , y = 230)

    #

    entry2_2 = Entry(top, width = 50)
    entry2_2.config(font=('Arial', 12))
    entry2_2.pack(pady = 5)
    entry2_2.place(x = 510,y = 270)


    button3_2 = Button(top, text='Cancel', font=('Helvetica', 14),bg = 'red', command=cancel)
    button3_2.pack()
    button3_2.place(x=890, y=300)



    button4_2 = Button(top, text='Enter', font=('Helvetica', 14),bg = 'green', command = page_3)
    button4_2.pack()
    button4_2.place(x=510, y=300)


#==================Login Page===================


l = Label(top, text="Welcome To Pharmacy Management System", fg='green')
l.config(font=('Arial', 39, 'bold'))
l.pack()

# lbl = Label(top,text = 'Welcome to Medicine Search',font= ("Times",20),fg = 'green')
# lbl.pack(pady = 10)

photo2 = PhotoImage(file = 'login.png')
photo = Label(top,image = photo2, bg = 'white')
photo.pack()
photo.place(x = 0 ,y = 100)


button2 = Button(top, text = 'Login as General Member',font =('Helvetica',18),bg = 'yellow' ,command = log_gen)
button2.pack()
button2.place(x = 420 ,y = 100 )

button4 = Button(top, text = 'Login as Worker',font =('Helvetica',18),bg = 'yellow',command = log_work)
button4.pack()
button4.place(x = 780 ,y = 100 )

top.mainloop()




