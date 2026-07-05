---
type: Jurisdiction
title: "Johnston County, NC"
classification: county
fips: "37101"
state: "NC"
demographics:
  population: 234263
  population_under_18: 58336
  population_18_64: 143779
  population_65_plus: 32148
  median_household_income: 83384
  poverty_rate: 10.63
  homeownership_rate: 76.05
  unemployment_rate: 3.81
  median_home_value: 305600
  gini_index: 0.4208
  vacancy_rate: 6.17
  race_white: 150425
  race_black: 39604
  race_asian: 1948
  race_native: 2293
  hispanic: 39336
  bachelors_plus: 58326
districts:
  - to: "us/states/nc/districts/13"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/nc/districts/senate/10"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/28"
    rel: in-district
    area_weight: 0.6514
  - to: "us/states/nc/districts/house/26"
    rel: in-district
    area_weight: 0.2538
  - to: "us/states/nc/districts/house/53"
    rel: in-district
    area_weight: 0.0946
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Johnston County, NC

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 234263 |
| Under 18 | 58336 |
| 18–64 | 143779 |
| 65+ | 32148 |
| Median household income | 83384 |
| Poverty rate | 10.63 |
| Homeownership rate | 76.05 |
| Unemployment rate | 3.81 |
| Median home value | 305600 |
| Gini index | 0.4208 |
| Vacancy rate | 6.17 |
| White | 150425 |
| Black | 39604 |
| Asian | 1948 |
| Native | 2293 |
| Hispanic/Latino | 39336 |
| Bachelor's or higher | 58326 |

## Districts

- [NC-13](/us/states/nc/districts/13.md) — 100% (congressional)
- [NC Senate District 10](/us/states/nc/districts/senate/10.md) — 100% (state senate)
- [NC House District 28](/us/states/nc/districts/house/28.md) — 65% (state house)
- [NC House District 26](/us/states/nc/districts/house/26.md) — 25% (state house)
- [NC House District 53](/us/states/nc/districts/house/53.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
