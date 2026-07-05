---
type: Jurisdiction
title: "Martin County, NC"
classification: county
fips: "37117"
state: "NC"
demographics:
  population: 21644
  population_under_18: 4399
  population_18_64: 11713
  population_65_plus: 5532
  median_household_income: 48578
  poverty_rate: 20.37
  homeownership_rate: 66.79
  unemployment_rate: 6.13
  median_home_value: 109700
  gini_index: 0.4476
  vacancy_rate: 14.07
  race_white: 11137
  race_black: 8723
  race_asian: 120
  race_native: 16
  hispanic: 963
  bachelors_plus: 3344
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nc/districts/senate/2"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nc/districts/house/23"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Martin County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21644 |
| Under 18 | 4399 |
| 18–64 | 11713 |
| 65+ | 5532 |
| Median household income | 48578 |
| Poverty rate | 20.37 |
| Homeownership rate | 66.79 |
| Unemployment rate | 6.13 |
| Median home value | 109700 |
| Gini index | 0.4476 |
| Vacancy rate | 14.07 |
| White | 11137 |
| Black | 8723 |
| Asian | 120 |
| Native | 16 |
| Hispanic/Latino | 963 |
| Bachelor's or higher | 3344 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 100% (congressional)
- [NC Senate District 2](/us/states/nc/districts/senate/2.md) — 100% (state senate)
- [NC House District 23](/us/states/nc/districts/house/23.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
