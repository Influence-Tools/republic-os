---
type: Jurisdiction
title: "Wayne County, NC"
classification: county
fips: "37191"
state: "NC"
demographics:
  population: 118652
  population_under_18: 28014
  population_18_64: 70376
  population_65_plus: 20262
  median_household_income: 59733
  poverty_rate: 17.33
  homeownership_rate: 61.45
  unemployment_rate: 5.21
  median_home_value: 178700
  gini_index: 0.4487
  vacancy_rate: 11.21
  race_white: 60942
  race_black: 35324
  race_asian: 1430
  race_native: 112
  hispanic: 16280
  bachelors_plus: 22409
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/nc/districts/senate/4"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nc/districts/house/10"
    rel: in-district
    area_weight: 0.5411
  - to: "us/states/nc/districts/house/4"
    rel: in-district
    area_weight: 0.4588
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Wayne County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 118652 |
| Under 18 | 28014 |
| 18–64 | 70376 |
| 65+ | 20262 |
| Median household income | 59733 |
| Poverty rate | 17.33 |
| Homeownership rate | 61.45 |
| Unemployment rate | 5.21 |
| Median home value | 178700 |
| Gini index | 0.4487 |
| Vacancy rate | 11.21 |
| White | 60942 |
| Black | 35324 |
| Asian | 1430 |
| Native | 112 |
| Hispanic/Latino | 16280 |
| Bachelor's or higher | 22409 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 100% (congressional)
- [NC Senate District 4](/us/states/nc/districts/senate/4.md) — 100% (state senate)
- [NC House District 10](/us/states/nc/districts/house/10.md) — 54% (state house)
- [NC House District 4](/us/states/nc/districts/house/4.md) — 46% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
