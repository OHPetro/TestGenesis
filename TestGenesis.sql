select category_name,AVG(cost) as cost_avg from adverts
join costs on adverts.advert_id = costs.advert_id
group by category_name
having cost_abg < 500;
