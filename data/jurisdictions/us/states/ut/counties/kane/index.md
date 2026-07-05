---
type: Jurisdiction
title: "Kane County, UT"
classification: county
fips: "49025"
state: "UT"
demographics:
  population: 8170
  population_under_18: 1697
  population_18_64: 4455
  population_65_plus: 2018
  median_household_income: 77092
  poverty_rate: 9.53
  homeownership_rate: 80.41
  unemployment_rate: 3.69
  median_home_value: 410900
  gini_index: 0.407
  vacancy_rate: 46.18
  race_white: 7310
  race_black: 17
  race_asian: 9
  race_native: 189
  hispanic: 409
  bachelors_plus: 2201
districts:
  - to: "us/states/ut/districts/02"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ut/districts/senate/26"
    rel: in-district
    area_weight: 0.7692
  - to: "us/states/ut/districts/senate/27"
    rel: in-district
    area_weight: 0.2307
  - to: "us/states/ut/districts/house/69"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Kane County, UT

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8170 |
| Under 18 | 1697 |
| 18–64 | 4455 |
| 65+ | 2018 |
| Median household income | 77092 |
| Poverty rate | 9.53 |
| Homeownership rate | 80.41 |
| Unemployment rate | 3.69 |
| Median home value | 410900 |
| Gini index | 0.407 |
| Vacancy rate | 46.18 |
| White | 7310 |
| Black | 17 |
| Asian | 9 |
| Native | 189 |
| Hispanic/Latino | 409 |
| Bachelor's or higher | 2201 |

## Districts

- [UT-02](/us/states/ut/districts/02.md) — 100% (congressional)
- [UT Senate District 26](/us/states/ut/districts/senate/26.md) — 77% (state senate)
- [UT Senate District 27](/us/states/ut/districts/senate/27.md) — 23% (state senate)
- [UT House District 69](/us/states/ut/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
