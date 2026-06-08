# Write your MySQL query statement below
select current_day.id from Weather as current_day 
where exists(
    select 1
    from Weather as yesterday
    where current_day.temperature > yesterday.temperature
    and current_day.recordDate = yesterday.recordDate + INTERVAL 1 DAY
)