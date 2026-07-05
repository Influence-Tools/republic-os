---
type: Jurisdiction
title: "Greene County, NC"
classification: county
fips: "37079"
state: "NC"
demographics:
  population: 20486
  population_under_18: 3862
  population_18_64: 13080
  population_65_plus: 3544
  median_household_income: 53244
  poverty_rate: 21.05
  homeownership_rate: 66.51
  unemployment_rate: 5.65
  median_home_value: 117400
  gini_index: 0.3916
  vacancy_rate: 12.94
  race_white: 9811
  race_black: 6514
  race_asian: 10
  race_native: 221
  hispanic: 3166
  bachelors_plus: 2227
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.9967
  - to: "us/states/nc/districts/senate/4"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/nc/districts/house/12"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Greene County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20486 |
| Under 18 | 3862 |
| 18–64 | 13080 |
| 65+ | 3544 |
| Median household income | 53244 |
| Poverty rate | 21.05 |
| Homeownership rate | 66.51 |
| Unemployment rate | 5.65 |
| Median home value | 117400 |
| Gini index | 0.3916 |
| Vacancy rate | 12.94 |
| White | 9811 |
| Black | 6514 |
| Asian | 10 |
| Native | 221 |
| Hispanic/Latino | 3166 |
| Bachelor's or higher | 2227 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 100% (congressional)
- [NC Senate District 4](/us/states/nc/districts/senate/4.md) — 100% (state senate)
- [NC House District 12](/us/states/nc/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
