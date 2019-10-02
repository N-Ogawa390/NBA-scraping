from self_mod.init_mods import *

class Player:
    def __init__(self, num):
        wtpath('//div[contains(@class,"player-list")]')
        naming = br.find_element_by_xpath(f'//div[contains(@class,"player-list")]/div[{num}]/div[3]/a').text

        wtpath('//div[contains(@class,"player-list")]')
        br.find_element_by_xpath(f'//div[contains(@class,"player-list")]/div[{num}]/div[3]/a').click()

        self.NAME = naming

        self.setability('PPG')
        self.PPG = Decimal(self.ability)

        self.setability('OFF')
        self.OFF = Decimal(self.ability)

        self.setability('TO')
        self.TO = Decimal(self.ability)

        self.setability('SPG')
        self.SPG = Decimal(self.ability)

        self.setability('DEF')
        self.DEF = Decimal(self.ability)

        self.offpoint = self.PPG + self.OFF * 4 - self.TO * 4
        self.defpoint = self.SPG * 4 + self.DEF * 2

        br.back()

    def setability(self, abilities):
        wtpath('//table[@class="sib-zebra-stripes no-sort"]')
        time.sleep(1)
        tblth = br.find_elements_by_xpath('//table[@class="sib-zebra-stripes no-sort"]/thead//tr/th')
        tblthtx = []
        for i in tblth:
            tblthtx.append(i.text)

        num = tblthtx.index(abilities) + 2

        tbltd = br.find_elements_by_xpath('//table[@class="sib-zebra-stripes no-sort"]/tbody/tr[2]/td')
        tbltdtx = []
        for i in tbltd:
            tbltdtx.append(i.text)
        self.ability = br.find_element_by_xpath(f'//table[@class="sib-zebra-stripes no-sort"]/tbody/tr[2]/td[{num}]').text

print('作業を始めます！')
br.get('https://jp.global.nba.com/standings/')

tmlist = {}

howmanytm = br.find_elements_by_xpath('//section//nba-stat-table[2]//div[@class="nba-stat-table__overlay"]//tbody/tr')

wtpath('//div[@class="main-nav-container container"]')
for i in range(1, len(howmanytm) + 1):
    tmlist[i] = br.find_element_by_xpath(f'//section//nba-stat-table[2]//tbody//tr[{i}]/td[4]/a').text

for i, v in tmlist.items():
    print(str(i) + '：' + v)

tm = input('調査したいチームの番号を入力してください：')

tmname = tmlist[int(tm)]
print('それでは『' + tmname + '』の選手について調査しますね！\n少しお待ちください！')

br.find_element_by_xpath(f'//section//nba-stat-table[2]//tbody/tr[{tm}]/td[4]/a').click()

wtpath('//div[contains(@class,"player-list")]')
player1 = Player(1)
player2 = Player(2)
player3 = Player(3)
player4 = Player(4)
player5 = Player(5)

the_team = [player1, player2, player3, player4, player5]

print('\n' + player1.NAME + '\nオフェンス能力：' + str(player1.offpoint) + '\nディフェンス能力：' + str(player1.defpoint))
print('\n' + player2.NAME + '\nオフェンス能力：' + str(player2.offpoint) + '\nディフェンス能力：' + str(player2.defpoint))
print('\n' + player3.NAME + '\nオフェンス能力：' + str(player3.offpoint) + '\nディフェンス能力：' + str(player3.defpoint))
print('\n' + player4.NAME + '\nオフェンス能力：' + str(player4.offpoint) + '\nディフェンス能力：' + str(player4.defpoint))
print('\n' + player5.NAME + '\nオフェンス能力：' + str(player5.offpoint) + '\nディフェンス能力：' + str(player5.defpoint))

print('\n【チーム総合力】\nオフェンス能力：' + str((player1.offpoint + player2.offpoint + player3.offpoint + player4.offpoint + player5.offpoint) / 5) + '\nディフェンス能力：' + str((player1.defpoint + player2.defpoint + player3.defpoint + player4.defpoint + player5.defpoint) / 5))

while True:
    for i in the_team:
        print(f'\n{the_team.index(i) + 1}：{i.NAME}')
    choice = input('さらに詳しく知りたい選手がいる場合は選手の番号を入力してください！\nいない場合は『no』と入力してね：')
    if choice == 'no':
        break
    elif int(choice) == 1 or 2 or 3 or 4 or 5:
        print('\n■' + the_team[int(choice) - 1].NAME + '\n～試合平均～')
        print('得点：' + str(the_team[int(choice) - 1].PPG))
        print('オフェンスリバウンド：' + str(the_team[int(choice) - 1].OFF))
        print('ターンノーバー：' + str(the_team[int(choice) - 1].TO))
        print('スティール：' + str(the_team[int(choice) - 1].SPG))
        print('ディフェンスリバウンド：' + str(the_team[int(choice) - 1].DEF))
        time.sleep(2)
    else:
        print('※入力が正しくありません※')

print('それでは処理を終了します。お疲れ様でした。\n※5秒後にクローズします。')
time.sleep(5)
br.close()
br.quit()
sys.exit()
