---
type: Jurisdiction
title: "Durham County, NC"
classification: county
fips: "37063"
state: "NC"
demographics:
  population: 332353
  population_under_18: 66603
  population_18_64: 217586
  population_65_plus: 48164
  median_household_income: 82316
  poverty_rate: 11.51
  homeownership_rate: 55.5
  unemployment_rate: 3.91
  median_home_value: 389400
  gini_index: 0.4623
  vacancy_rate: 7.3
  race_white: 144356
  race_black: 106591
  race_asian: 17932
  race_native: 2258
  hispanic: 52523
  bachelors_plus: 189392
districts:
  - to: "us/states/nc/districts/04"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/nc/districts/senate/22"
    rel: in-district
    area_weight: 0.7447
  - to: "us/states/nc/districts/senate/20"
    rel: in-district
    area_weight: 0.2549
  - to: "us/states/nc/districts/house/2"
    rel: in-district
    area_weight: 0.4461
  - to: "us/states/nc/districts/house/31"
    rel: in-district
    area_weight: 0.2735
  - to: "us/states/nc/districts/house/29"
    rel: in-district
    area_weight: 0.1513
  - to: "us/states/nc/districts/house/30"
    rel: in-district
    area_weight: 0.1288
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Durham County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 332353 |
| Under 18 | 66603 |
| 18–64 | 217586 |
| 65+ | 48164 |
| Median household income | 82316 |
| Poverty rate | 11.51 |
| Homeownership rate | 55.5 |
| Unemployment rate | 3.91 |
| Median home value | 389400 |
| Gini index | 0.4623 |
| Vacancy rate | 7.3 |
| White | 144356 |
| Black | 106591 |
| Asian | 17932 |
| Native | 2258 |
| Hispanic/Latino | 52523 |
| Bachelor's or higher | 189392 |

## Districts

- [NC-04](/us/states/nc/districts/04.md) — 100% (congressional)
- [NC Senate District 22](/us/states/nc/districts/senate/22.md) — 74% (state senate)
- [NC Senate District 20](/us/states/nc/districts/senate/20.md) — 25% (state senate)
- [NC House District 2](/us/states/nc/districts/house/2.md) — 45% (state house)
- [NC House District 31](/us/states/nc/districts/house/31.md) — 27% (state house)
- [NC House District 29](/us/states/nc/districts/house/29.md) — 15% (state house)
- [NC House District 30](/us/states/nc/districts/house/30.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
