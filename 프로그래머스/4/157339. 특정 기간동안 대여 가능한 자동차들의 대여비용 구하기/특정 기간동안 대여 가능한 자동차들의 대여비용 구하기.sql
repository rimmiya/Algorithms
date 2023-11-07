SELECT C.CAR_ID, C.CAR_TYPE, ROUND(C.DAILY_FEE * 30 * (100 - P.DISCOUNT_RATE) / 100) AS FEE
FROM CAR_RENTAL_COMPANY_CAR AS C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H ON C.CAR_ID = H.CAR_ID
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P ON C.CAR_TYPE = P.CAR_TYPE
WHERE C.CAR_ID NOT IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE > '2022-11-01' AND START_DATE < '2022-12-01'
) AND C.CAR_TYPE IN ('세단', 'SUV') AND P.DURATION_TYPE = '30일 이상'
GROUP BY C.CAR_ID
HAVING (FEE >= 500000 AND FEE < 2000000) 
ORDER BY FEE DESC, C.CAR_TYPE ASC, C.CAR_ID DESC