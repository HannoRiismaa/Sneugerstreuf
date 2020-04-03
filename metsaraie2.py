from durable.lang import *

with ruleset('test'):
    @when_any(m.Arenguklass == 'Noorendik')
    def ei_raie_noorendik(c):
        print('Raiumisotsus: Ei, sest arengusklass on {0}'.format(c.m.Arenguklass))
        
    @when_any ((m.Arenguklass == 'latimets') & (m.Puudearv < 30000), (m.Arenguklass == 'noorendik'), (m.Looduskaitsealune == 'jah'))
    def ei_raie(c):
        print ('Raiumisotsus:Ei. Lopeta kogu too.')
    
    @when_all ((m.Arenguklass == 'latimets') & (m.Puudearv > 30000))
    def jah_raie(c):
        print ('Raiumisotsus:Jah. Raietuup: Valgustusraie')
    
    @when_any(m.Linnurahu == 'jah')
    def ei_raie_linnurahu(c):
        print('Raiumisotsus:Ei. Tegemist on linnurahuga.')
        
    @when_all ((m.Arenguklass == 'latimets') & (m.Diameeter > 6))
    def harvendusraie(c):
        print ('Raiumisotsus:Jah. Raietuup: Harvendusraie. Puu diameeter:{0}'.format(c.m.Diameeter))
        Vanus = c.m.Vanus;
        peapuuliik = c.m.Peapuuliik;
        if((30<=Vanus<=40) and peapuuliik=='Mand'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on mand JA vanus 30- 40 aastat SIIS raiemaht on 1/3 tagavara')
        if((Vanus>40) and peapuuliik=='Mand'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on mand JA vanus >40 SIIS raiemaht on 1/4 tagavara')
        if((Vanus<=30) and peapuuliik=='Mand'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on mand JA vanus <30 SIIS raiemaht on 1/2 tagavara')
        if((Vanus<=40) and peapuuliik=='Kuusk'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on kuusk JA vanus <40 aastat SIIS raiemaht on 2/3 tagavara')
        if((Vanus>40) and peapuuliik=='Kuusk'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on kuusk JA vanus >40 aastat SIIS raiemaht on 1/3 tagavara')
        if((Vanus<30) and peapuuliik=='Kask'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on kask JA vanus <30 aastat SIIS raiemaht on 2/3 tagavara')
        if((Vanus>30) and peapuuliik=='Kask'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on kask JA vanus >30 aastat SIIS raiemaht on 1/2 tagavara')
        if((Vanus<=30) and peapuuliik=='Haab'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on haab JA vanus <30 aastat SIIS raiemaht on 1/2 tagavara')
        if((Vanus>30) and peapuuliik=='Haab'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on haab JA vanus >30 aastat SIIS raiemaht on 1/3 tagavara')
            
    @when_all ((m.Arenguklass == 'Keskealine') | (m.Arenguklass=='Valmiv mets')|(m.Arenguklass=='Kupsmets'))
    def harvendusraie(c):
        print ('Raiumisotsus:Jah. Raietuup: Harvendusraie.')
        Vanus = c.m.Vanus;
        peapuuliik = c.m.Peapuuliik;
        if((30<Vanus<40) and peapuuliik=='Mand'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on mand JA vanus 30- 40 aastat SIIS raiemaht on 1/3 tagavara')
        if((Vanus>40) and peapuuliik=='Mand'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on mand JA vanus >40 SIIS raiemaht on 1/4 tagavara')
        if((Vanus<30) and peapuuliik=='Mand'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on mand JA vanus <30 SIIS raiemaht on 1/2 tagavara')
        if((Vanus<40) and peapuuliik=='Kuusk'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on kuusk JA vanus <40 aastat SIIS raiemaht on 2/3 tagavara')
        if((Vanus>40) and peapuuliik=='Kuusk'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on kuusk JA vanus >40 aastat SIIS raiemaht on 1/3 tagavara')
        if((Vanus<30) and peapuuliik=='Kask'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on kask JA vanus <30 aastat SIIS raiemaht on 2/3 tagavara')
        if((Vanus>30) and peapuuliik=='Kask'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on kask JA vanus >30 aastat SIIS raiemaht on 1/2 tagavara')
        if((Vanus<30) and peapuuliik=='Haab'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on haab JA vanus <30 aastat SIIS raiemaht on 1/2 tagavara')
        if((Vanus>30) and peapuuliik=='Haab'):
            print('Kuna raietuup on harvendusraie JA peapuuliik on haab JA vanus >30 aastat SIIS raiemaht on 1/3 tagavara')
            
    @when_all ((m.Peapuuliik == 'Mand')| (m.Peapuuliik == 'Lehis')| (m.Peapuuliik == 'Seedermand')&(m.Vanus >= 90)&(m.Boniteediklass =='1')|(m.Boniteediklass =='1A')|(m.Boniteediklass =='2'))
#    KUI raietuup on lageraie JA  kasvukoht on Leesikaloo voi Kastikuloo voi Lubikaloo voi Sambliku voi Kanarbiku voi Pohla voi Janesekapsa-pohla voi Mustika voi Karusambla-mustika voi Tarna voi Sinika voi Karusambla voi Siirdesoo voi Raba  SIIS istuta asemele mand  
#
#KUI raietuup on lageraie JA kasvukoht on Janesekapsa-mustika voi Janesekapsa voi Sinilille SIIS istuta asemele kuusk 
#
#KUI raietuup on lageraie JA kasvukoht on Angervaksa voi Madalsoo voi Sonajala voi Osja SIIS istuta asemele kask  
#
#KUI raietuup on lageraie JA kasvukoht on Lodu SIIS  istuta asemele sanglepp 
#
#KUI raietuup on lageraie JA kasvukoht on Kodusood SIIS istuta asemele mand voi kuusk 
#
#KUI raietuup on lageraie JA kasvukoht on Tarna-angervaksa SIIS istuta asemele kask  voi mand 
#
#KUI raietuup on lageraie JA kasvukoht on Naadi SIIS istuta asemele kask voi  kuusk
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietuup: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        Kasvukoht = c.m.Kasvukoht;
        if(Kasvukoht in('Leesikaloo','Kastikuloo','Lubikaloo','Sambliku','Kanarbiku','Pohla','Janesekapsa-pohla','Mustika','Karusambla-mustika','Tarna','Sinika','Karusambla','Siirdesoo','Raba')):
            print('Kuna kasvukoht on {0}, siis istuta asemele mand'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Janesekapsa-mustika','Janesekapsa','Sinilille')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Angervaksa','Madalsoo','Sonajala','Osja')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Kodusood')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Tarna-angervaksa')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Naadi')):
            print('Kuna kasvukoht on {0}, siis istuta asemele kuusk voi kask'.format(c.m.Kasvukoht))
        
    @when_all ((m.Peapuuliik == 'Mand')| (m.Peapuuliik == 'Lehis')| (m.Peapuuliik == 'Seedermand')&(m.Vanus >= 100)&(m.Boniteediklass =='3'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietuup: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        Kasvukoht = c.m.Kasvukoht;
        if(Kasvukoht in('Leesikaloo','Kastikuloo','Lubikaloo','Sambliku','Kanarbiku','Pohla','Janesekapsa-pohla','Mustika','Karusambla-mustika','Tarna','Sinika','Karusambla','Siirdesoo','Raba')):
            print('Kuna kasvukoht on {0}, siis istuta asemele mand'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Janesekapsa-mustika','Janesekapsa','Sinilille')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Angervaksa','Madalsoo','Sonajala','Osja')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Kodusood')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Tarna-angervaksa')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Naadi')):
            print('Kuna kasvukoht on {0}, siis istuta asemele kuusk voi kask'.format(c.m.Kasvukoht))
    
    @when_all ((m.Peapuuliik == 'Mand')| (m.Peapuuliik == 'Lehis')| (m.Peapuuliik == 'Seedermand')&(m.Vanus >= 110)&(m.Boniteediklass =='4'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietuup: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        Kasvukoht = c.m.Kasvukoht;
        if(Kasvukoht in('Leesikaloo','Kastikuloo','Lubikaloo','Sambliku','Kanarbiku','Pohla','Janesekapsa-pohla','Mustika','Karusambla-mustika','Tarna','Sinika','Karusambla','Siirdesoo','Raba')):
            print('Kuna kasvukoht on {0}, siis istuta asemele mand'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Janesekapsa-mustika','Janesekapsa','Sinilille')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Angervaksa','Madalsoo','Sonajala','Osja')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Kodusood')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Tarna-angervaksa')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Naadi')):
            print('Kuna kasvukoht on {0}, siis istuta asemele kuusk voi kask'.format(c.m.Kasvukoht))
        
    @when_all ((m.Peapuuliik == 'Mand')| (m.Peapuuliik == 'Lehis')| (m.Peapuuliik == 'Seedermand')&(m.Vanus >= 120)&(m.Boniteediklass =='5')|(m.Boniteediklass =='5A'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietuup: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        Kasvukoht = c.m.Kasvukoht;
        if(Kasvukoht in('Leesikaloo','Kastikuloo','Lubikaloo','Sambliku','Kanarbiku','Pohla','Janesekapsa-pohla','Mustika','Karusambla-mustika','Tarna','Sinika','Karusambla','Siirdesoo','Raba')):
            print('Kuna kasvukoht on {0}, siis istuta asemele mand'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Janesekapsa-mustika','Janesekapsa','Sinilille')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Angervaksa','Madalsoo','Sonajala','Osja')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Kodusood')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Tarna-angervaksa')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Naadi')):
            print('Kuna kasvukoht on {0}, siis istuta asemele kuusk voi kask'.format(c.m.Kasvukoht))
        
    @when_all (((m.Peapuuliik == 'Kuusk')| (m.Peapuuliik=='Nulg') | (m.Peapuuliik=='Ebatsuuga'))&(m.Vanus >= 80)&(m.Boniteediklass =='1')|(m.Boniteediklass =='1A')|(m.Boniteediklass =='2'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietuup: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        Kasvukoht = c.m.Kasvukoht;
        if(Kasvukoht in('Leesikaloo','Kastikuloo','Lubikaloo','Sambliku','Kanarbiku','Pohla','Janesekapsa-pohla','Mustika','Karusambla-mustika','Tarna','Sinika','Karusambla','Siirdesoo','Raba')):
            print('Kuna kasvukoht on {0}, siis istuta asemele mand'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Janesekapsa-mustika','Janesekapsa','Sinilille')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Angervaksa','Madalsoo','Sonajala','Osja')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Kodusood')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Tarna-angervaksa')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Naadi')):
            print('Kuna kasvukoht on {0}, siis istuta asemele kuusk voi kask'.format(c.m.Kasvukoht))
        
    @when_all (((m.Peapuuliik == 'Kuusk')| (m.Peapuuliik=='Nulg') | (m.Peapuuliik=='Ebatsuuga'))&(m.Vanus >= 90)&(m.Boniteediklass =='3')|(m.Boniteediklass =='4')|(m.Boniteediklass =='5')|(m.Boniteediklass =='5A'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietuup: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        Kasvukoht = c.m.Kasvukoht;
        if(Kasvukoht in('Leesikaloo','Kastikuloo','Lubikaloo','Sambliku','Kanarbiku','Pohla','Janesekapsa-pohla','Mustika','Karusambla-mustika','Tarna','Sinika','Karusambla','Siirdesoo','Raba')):
            print('Kuna kasvukoht on {0}, siis istuta asemele mand'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Janesekapsa-mustika','Janesekapsa','Sinilille')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Angervaksa','Madalsoo','Sonajala','Osja')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Kodusood')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Tarna-angervaksa')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Naadi')):
            print('Kuna kasvukoht on {0}, siis istuta asemele kuusk voi kask'.format(c.m.Kasvukoht))
    
    @when_all ((m.Peapuuliik == 'Kask')&(m.Vanus >= 60)&((m.Boniteediklass =='1A')|(m.Boniteediklass =='1')))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietuup: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        Kasvukoht = c.m.Kasvukoht;
        if(Kasvukoht in('Leesikaloo','Kastikuloo','Lubikaloo','Sambliku','Kanarbiku','Pohla','Janesekapsa-pohla','Mustika','Karusambla-mustika','Tarna','Sinika','Karusambla','Siirdesoo','Raba')):
            print('Kuna kasvukoht on {0}, siis istuta asemele mand'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Janesekapsa-mustika','Janesekapsa','Sinilille')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Angervaksa','Madalsoo','Sonajala','Osja')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Kodusood')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Tarna-angervaksa')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Naadi')):
            print('Kuna kasvukoht on {0}, siis istuta asemele kuusk voi kask'.format(c.m.Kasvukoht))
        
    @when_all ((m.Peapuuliik == 'Kask')&(m.Vanus >= 70)&((m.Boniteediklass =='2')|(m.Boniteediklass =='3')|(m.Boniteediklass =='5A')|(m.Boniteediklass =='4')|(m.Boniteediklass =='5')))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietuup: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        Kasvukoht = c.m.Kasvukoht;
        if(Kasvukoht in('Leesikaloo','Kastikuloo','Lubikaloo','Sambliku','Kanarbiku','Pohla','Janesekapsa-pohla','Mustika','Karusambla-mustika','Tarna','Sinika','Karusambla','Siirdesoo','Raba')):
            print('Kuna kasvukoht on {0}, siis istuta asemele mand'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Janesekapsa-mustika','Janesekapsa','Sinilille')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Angervaksa','Madalsoo','Sonajala','Osja')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Kodusood')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Tarna-angervaksa')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Naadi')):
            print('Kuna kasvukoht on {0}, siis istuta asemele kuusk voi kask'.format(c.m.Kasvukoht))
        str = str(m.Raiekpv)
        print(str)
        
    @when_all (((m.Peapuuliik == 'Haab')| (m.Peapuuliik=='Pappel') | (m.Peapuuliik=='Pihlakas'))&(m.Vanus >= 30)&(m.Boniteediklass =='1A'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietuup: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        Kasvukoht = c.m.Kasvukoht;
        if(Kasvukoht in('Leesikaloo','Kastikuloo','Lubikaloo','Sambliku','Kanarbiku','Pohla','Janesekapsa-pohla','Mustika','Karusambla-mustika','Tarna','Sinika','Karusambla','Siirdesoo','Raba')):
            print('Kuna kasvukoht on {0}, siis istuta asemele mand'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Janesekapsa-mustika','Janesekapsa','Sinilille')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Angervaksa','Madalsoo','Sonajala','Osja')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Kodusood')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Tarna-angervaksa')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Naadi')):
            print('Kuna kasvukoht on {0}, siis istuta asemele kuusk voi kask'.format(c.m.Kasvukoht))
        
    @when_all (((m.Peapuuliik == 'Haab')| (m.Peapuuliik=='Pappel') | (m.Peapuuliik=='Pihlakas'))&(m.Vanus >= 40)&(m.Boniteediklass =='1')|(m.Boniteediklass =='2'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietuup: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        Kasvukoht = c.m.Kasvukoht;
        if(Kasvukoht in('Leesikaloo','Kastikuloo','Lubikaloo','Sambliku','Kanarbiku','Pohla','Janesekapsa-pohla','Mustika','Karusambla-mustika','Tarna','Sinika','Karusambla','Siirdesoo','Raba')):
            print('Kuna kasvukoht on {0}, siis istuta asemele mand'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Janesekapsa-mustika','Janesekapsa','Sinilille')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Angervaksa','Madalsoo','Sonajala','Osja')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Kodusood')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Tarna-angervaksa')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Naadi')):
            print('Kuna kasvukoht on {0}, siis istuta asemele kuusk voi kask'.format(c.m.Kasvukoht))
        
    @when_all (((m.Peapuuliik == 'Haab')| (m.Peapuuliik=='Pappel') | (m.Peapuuliik=='Pihlakas'))&(m.Vanus >= 50)&(m.Boniteediklass =='3')|(m.Boniteediklass =='4')|(m.Boniteediklass =='5')|(m.Boniteediklass =='5A'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietuup: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        Kasvukoht = c.m.Kasvukoht;
        if(Kasvukoht in('Leesikaloo','Kastikuloo','Lubikaloo','Sambliku','Kanarbiku','Pohla','Janesekapsa-pohla','Mustika','Karusambla-mustika','Tarna','Sinika','Karusambla','Siirdesoo','Raba')):
            print('Kuna kasvukoht on {0}, siis istuta asemele mand'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Janesekapsa-mustika','Janesekapsa','Sinilille')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Angervaksa','Madalsoo','Sonajala','Osja')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Kodusood')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Tarna-angervaksa')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Naadi')):
            print('Kuna kasvukoht on {0}, siis istuta asemele kuusk voi kask'.format(c.m.Kasvukoht))
        
    @when_all(m.Kahjustus == 'Nork')
    def ei_raie_kahjustatus(c):
        print('Raiumisotsus:Ei. Pohjuseks kahjustus: {0}'.format(c.m.Kahjustus))
        
    @when_any((m.Kahjustus == 'Keskmine') | (m.Kahjustus == 'Tugev') | (m.Kahjustus == 'Vaga tugev'))
    def ei_rai_kahjustatus(c):
        print ('Raiumisotsus:Jah. Raietuup: Sanitaarraie. Kahjustatus on {0}'.format(c.m.Kahjustus))
        
    @when_all ((m.Peapuuliik == 'Sanglepp')&(m.Vanus >= 60))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietuup: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        Kasvukoht = c.m.Kasvukoht;
        if(Kasvukoht in('Leesikaloo','Kastikuloo','Lubikaloo','Sambliku','Kanarbiku','Pohla','Janesekapsa-pohla','Mustika','Karusambla-mustika','Tarna','Sinika','Karusambla','Siirdesoo','Raba')):
            print('Kuna kasvukoht on {0}, siis istuta asemele mand'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Janesekapsa-mustika','Janesekapsa','Sinilille')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Angervaksa','Madalsoo','Sonajala','Osja')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Kodusood')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Tarna-angervaksa')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Naadi')):
            print('Kuna kasvukoht on {0}, siis istuta asemele kuusk voi kask'.format(c.m.Kasvukoht))
        
    @when_all ((m.Peapuuliik == 'Hall-lepp')&(m.Vanus >= 30))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietuup: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        Kasvukoht = c.m.Kasvukoht;
        if(Kasvukoht in('Leesikaloo','Kastikuloo','Lubikaloo','Sambliku','Kanarbiku','Pohla','Janesekapsa-pohla','Mustika','Karusambla-mustika','Tarna','Sinika','Karusambla','Siirdesoo','Raba')):
            print('Kuna kasvukoht on {0}, siis istuta asemele mand'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Janesekapsa-mustika','Janesekapsa','Sinilille')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Angervaksa','Madalsoo','Sonajala','Osja')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Kodusood')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kuusk'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Tarna-angervaksa')):
            print('Kuna kasvukoht on {0}, siis istuta asemele Mand voi kask'.format(c.m.Kasvukoht))
        if(Kasvukoht in('Naadi')):
            print('Kuna kasvukoht on {0}, siis istuta asemele kuusk voi kask'.format(c.m.Kasvukoht))

post('test', {'Arenguklass':'latimets',
              'Peapuuliik':'Mand',
              'Vanus':93,
              'Boniteediklass':'1',
              'Kasvukoht':'Naadi' }) 
            
post('test', {'Peapuuliik' : 'Haab',
              'Vanus':30,  
              'Boniteediklass':'1A' })