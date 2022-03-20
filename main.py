deduction_max=18000
basicallow=132000
jointallow=264000
rate1=0.02
rate2=0.06
rate3=0.10
rate4=0.14
rate5=0.17
standardtax=0.15

class Tax_cal():

    def Malempfdeduct_cal(self, Mtotalincome):
        if Mtotalincome < 7100*12:
            mpfdeducted1 = 0
        elif Mtotalincome*0.05 >= 18000:
            mpfdeducted1 = 18000
        else:
            mpfdeducted1 = Mtotalincome*0.05

        afterMPF_M_income = Mtotalincome- mpfdeducted1
        return afterMPF_M_income

    def Femalempfdeduct_cal(self, Ftotalincome):
        if Ftotalincome < 7100*12:
            mpfdeducted2 = 0
        elif Ftotalincome*0.05 >= 18000:
            mpfdeducted2 = 18000
        else:
            mpfdeducted2 = Ftotalincome*0.05

        afterMPF_F_income = Ftotalincome - mpfdeducted2
        return afterMPF_F_income

    def Male_net_chargeable_income(self, Malempfdeduct_cal):
        if Malempfdeduct_cal < basicallow:
            m_n_c_i = 0
        elif Malempfdeduct_cal > basicallow:
            m_n_c_i = Malempfdeduct_cal - basicallow
        return m_n_c_i

    def Female_net_chargeable_income(self, Femalempfdeduct_cal):
        if Femalempfdeduct_cal < basicallow:
            f_n_c_i = 0
        elif Femalempfdeduct_cal > basicallow:
                f_n_c_i = Femalempfdeduct_cal - basicallow
        return f_n_c_i

    def Joint_net_chargeable_income(self,Malempfdeduct_cal,Femalempfdeduct_cal):
        before_j_n_c_i = Malempfdeduct_cal + Femalempfdeduct_cal
        if before_j_n_c_i < jointallow:
            j_n_c_i = 0
        elif before_j_n_c_i > jointallow:
            j_n_c_i = before_j_n_c_i - jointallow
        return j_n_c_i

    def male_tax_payable(self,BTax_Male):
        if BTax_Male in range(0,50000):
            MaleTax = BTax_Male * rate1
        elif BTax_Male in range(50001,100000):
            MaleTax = 50000*rate1 + (BTax_Male-50000)*rate2
        elif BTax_Male in range(100001,150000):
            MaleTax = 50000*rate1 + 50000*rate2 + (BTax_Male-100000)*rate3
        elif BTax_Male in range(150001,200000):
            MaleTax = 50000 * rate1 + 50000 * rate2 + 50000 * rate3 + (BTax_Male-150000)*rate4
        else:
            MaleTax = 50000 * rate1 + 50000 * rate2 + 50000 * rate3 + 50000 * rate4 + (BTax_Male-200000)*rate5
        return MaleTax

    def female_tax_payable(self,BTax_Female):
        if BTax_Female in range(0,50000):
            FemaleTax = BTax_Female * rate1
        elif BTax_Female in range(50001,100000):
            FemaleTax = 50000*rate1 + (BTax_Female-50000)*rate2
        elif BTax_Female in range(100001,150000):
            FemaleTax = 50000*rate1 + 50000*rate2 + (BTax_Female-100000)*rate3
        elif BTax_Female in range(150001,200000):
            FemaleTax = 50000 * rate1 + 50000 * rate2 + 50000 * rate3 + (BTax_Female-150000)*rate4
        else:
            FemaleTax = 50000 * rate1 + 50000 * rate2 + 50000 * rate3 + 50000 * rate4 + (BTax_Female-200000)*rate5
        return FemaleTax

    def PersonalTaxPayableBySelfandSpouse(self,female_tax_payable,male_tax_payable):
        Total_PersonalTax = female_tax_payable + male_tax_payable
        return Total_PersonalTax

    def joint_tax_cal(self,BTax_Joint):
        if BTax_Joint in range(0,50000):
            JointTax = BTax_Joint * rate1
        elif BTax_Joint in range(50001,100000):
            JointTax = 50000*rate1 + (BTax_Joint-50000)*rate2
        elif BTax_Joint in range(100001,150000):
            JointTax = 50000*rate1 + 50000*rate2 + (BTax_Joint-100000)*rate3
        elif BTax_Joint in range(150001,200000):
            JointTax = 50000 * rate1 + 50000 * rate2 + 50000 * rate3 + (BTax_Joint-150000)*rate4
        else:
            JointTax = 50000 * rate1 + 50000 * rate2 + 50000 * rate3 + 50000 * rate4 + (BTax_Joint-200000)*rate5
        return JointTax

    def single_allowance(self,basicallow):
        singleallowance = basicallow
        return singleallowance

    def joint_allowance(self,jointallow):
        jointallowance = jointallow
        return jointallowance

    def male_tax_payable_standard(self,afterMPF_M_income):
        MaleSRTax = afterMPF_M_income * standardtax
        return MaleSRTax

    def female_tax_payable_standard(self,afterMPF_F_income):
        FemaleSRTax = afterMPF_F_income * standardtax
        return FemaleSRTax

    def joint_tax_payable_standard(self,afterMPF_M_income,afterMPF_F_income):
        JointSRTax = (afterMPF_M_income + afterMPF_F_income) * standardtax
        return JointSRTax

    def compare_tax_male(self,MaleSRTax,MaleTax):
        if MaleSRTax < MaleTax:
            ftax_payable_male = MaleSRTax
            return ftax_payable_male, "Yes"
        elif MaleSRTax >= MaleTax:
            ftax_payable_male = MaleTax
            return ftax_payable_male, "No"

    def compare_tax_female(self,FemaleSRTax,FemaleTax):
        if FemaleSRTax < FemaleTax:
            ftax_payable_female = FemaleSRTax
            return ftax_payable_female, "Yes"
        elif FemaleSRTax >= FemaleTax:
            ftax_payable_female = FemaleTax
            return ftax_payable_female, "No"

    def compare_joint(self,JointSRTax,JointTax):
        if JointSRTax < JointTax:
            fjoint_payable = JointSRTax
            return fjoint_payable, "Yes"
        elif JointSRTax > JointTax:
            fjoint_payable = JointTax
            return fjoint_payable, "No"

    def single(self,income):
        afterMPF_M_income = (self.Malempfdeduct_cal(income))
        m_n_c_i = self.Male_net_chargeable_income(afterMPF_M_income)
        MaleTax = self.male_tax_payable(m_n_c_i)
        MaleSRTax= self.male_tax_payable_standard(afterMPF_M_income)
        Male_Tax = self.compare_tax_male(MaleSRTax,MaleTax)
        singlea = self.single_allowance(basicallow)
        return(income, int(afterMPF_M_income),int(singlea), int(m_n_c_i),int(Male_Tax[0]),Male_Tax[1])

    def joint(self,income1,income2):
        jointincome = income1 + income2
        afterMPF_M_income = (self.Malempfdeduct_cal(income1))
        afterMPF_F_income = (self.Femalempfdeduct_cal(income2))
        jointmpf = afterMPF_M_income + afterMPF_F_income
        JointNetChargeableIncome = self.Joint_net_chargeable_income(afterMPF_M_income, afterMPF_F_income)
        m_n_c_i = self.Male_net_chargeable_income(afterMPF_M_income)
        f_n_c_i = self.Female_net_chargeable_income(afterMPF_F_income)
        MaleTax = self.male_tax_payable(m_n_c_i)
        FemaleTax = self.female_tax_payable(f_n_c_i)
        JointTax = self.joint_tax_cal(JointNetChargeableIncome)
        JointSRTax = self.joint_tax_payable_standard(afterMPF_M_income,afterMPF_F_income)
        Joint_Tax = self.compare_joint(JointSRTax,JointTax)
        jointa = self.joint_allowance(jointallow)
        return(jointincome, int(jointmpf) ,int(jointa),int(JointNetChargeableIncome),int(Joint_Tax[0]),Joint_Tax[1])

    def compare(self,JointTax,MaleTax,FemaleTax):
        if JointTax > MaleTax + FemaleTax:
            return "Separated Assessment is recommended"
        elif JointTax < MaleTax + FemaleTax:
            return "Joint Tax Assessment is recommended"
        else:
            return "Both Tax Assessment are same"




calt = Tax_cal()
print(calt.single(3000000))
print(calt.single(400000))
print(calt.joint(3000000,400000))




"""
            if chargeable >= standardrate:
                standard_pay = self.standardrate_tax_payable(chargeable)
            else:
                standard_pay = normal_pay + 1
            if standard_pay <= normal_pay:
                return standard_pay, "* standard rate used", dummydeduct
            elif standard_pay > normal_pay:
                return normal_pay, "", dummydeduct
"""



""" calt = Tax_cal()
    afterMPF_M_income = (calt.Malempfdeduct_cal(Mtotalincome))
    print(afterMPF_M_income)
    afterMPF_F_income = (calt.Femalempfdeduct_cal(Ftotalincome))
    print(afterMPF_F_income)
    Tax_payable_ST1 = calt.check_standard_range_single(afterMPF_M_income)
    print(Tax_payable_ST1)
    Tax_payable_ST2 = calt.check_standard_range_married(afterMPF_M_income, afterMPF_F_income)
    print(Tax_payable_ST2)
    m_n_c_i = calt.Male_net_chargeable_income(afterMPF_M_income)
    print(m_n_c_i)
    f_n_c_i = calt.Female_net_chargeable_income(afterMPF_F_income)
    print(f_n_c_i)
    JointNetChargeableIncome = calt.Joint_net_chargeable_income(afterMPF_M_income, afterMPF_F_income)
    print(JointNetChargeableIncome)
    Male_Tax = calt.male_tax_payable(m_n_c_i)
    print(Male_Tax)
    Female_Tax = calt.female_tax_payable(f_n_c_i)
    print(Female_Tax)

    TotalPersonalTax = calt.PersonalTaxPayableBySelfandSpouse(Female_Tax, Male_Tax)
    print(TotalPersonalTax)

    JointTax = calt.joint_tax_cal(JointNetChargeableIncome)
    print(JointTax)"""





