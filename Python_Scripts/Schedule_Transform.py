import pandas as pd

schedule = pd.read_csv('2021-22 NBA Schedule.csv')

scheduleT = schedule.transpose()
scheduleT.columns = scheduleT.iloc[0]
scheduleT.drop(index=scheduleT.index[0], axis=0, inplace=True)

sched = scheduleT.where(scheduleT != 1, scheduleT.columns.to_series(), axis=1)
sched = sched.loc[:, sched.any()]

new_columns = [f'Gm {i}' for i in range(1, 83)]

new_schedule = []
i = 1
while (i <= len(sched.index)):
    print(i)
    test = sched.iloc[[i-1]]
    test1 = test.loc[:, (test != 0).any(axis=0)]
    test1.columns = new_columns
    test1 = test1.rename_axis('tm').reset_index()
    new_schedule.append(test1)
    i += 1

final_schedule = pd.concat(new_schedule)

#final_schedule.to_csv('C:/Users/aclark5/PycharmProjects/OttoneuBasketball/final_schedule.csv', index=False)
