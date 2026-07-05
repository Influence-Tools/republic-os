---
type: Jurisdiction
title: "Marshall County, WV"
classification: county
fips: "54051"
state: "WV"
demographics:
  population: 29865
  population_under_18: 5670
  population_18_64: 17100
  population_65_plus: 7095
  median_household_income: 59169
  poverty_rate: 16.82
  homeownership_rate: 78.43
  unemployment_rate: 4.31
  median_home_value: 149800
  gini_index: 0.4577
  vacancy_rate: 15.06
  race_white: 27801
  race_black: 98
  race_asian: 104
  race_native: 19
  hispanic: 347
  bachelors_plus: 6067
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/wv/districts/senate/1"
    rel: in-district
    area_weight: 0.6739
  - to: "us/states/wv/districts/senate/2"
    rel: in-district
    area_weight: 0.3255
  - to: "us/states/wv/districts/house/7"
    rel: in-district
    area_weight: 0.8493
  - to: "us/states/wv/districts/house/6"
    rel: in-district
    area_weight: 0.1497
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Marshall County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29865 |
| Under 18 | 5670 |
| 18–64 | 17100 |
| 65+ | 7095 |
| Median household income | 59169 |
| Poverty rate | 16.82 |
| Homeownership rate | 78.43 |
| Unemployment rate | 4.31 |
| Median home value | 149800 |
| Gini index | 0.4577 |
| Vacancy rate | 15.06 |
| White | 27801 |
| Black | 98 |
| Asian | 104 |
| Native | 19 |
| Hispanic/Latino | 347 |
| Bachelor's or higher | 6067 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 1](/us/states/wv/districts/senate/1.md) — 67% (state senate)
- [WV Senate District 2](/us/states/wv/districts/senate/2.md) — 33% (state senate)
- [WV House District 7](/us/states/wv/districts/house/7.md) — 85% (state house)
- [WV House District 6](/us/states/wv/districts/house/6.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
