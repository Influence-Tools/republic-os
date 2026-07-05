---
type: Jurisdiction
title: "Washington County, NC"
classification: county
fips: "37187"
state: "NC"
demographics:
  population: 10812
  population_under_18: 2064
  population_18_64: 5718
  population_65_plus: 3030
  median_household_income: 41813
  poverty_rate: 24.07
  homeownership_rate: 68.02
  unemployment_rate: 13.02
  median_home_value: 125900
  gini_index: 0.4976
  vacancy_rate: 21.46
  race_white: 4901
  race_black: 5182
  race_asian: 5
  race_native: 10
  hispanic: 436
  bachelors_plus: 1550
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.8925
  - to: "us/states/nc/districts/senate/2"
    rel: in-district
    area_weight: 0.888
  - to: "us/states/nc/districts/house/1"
    rel: in-district
    area_weight: 0.8881
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Washington County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10812 |
| Under 18 | 2064 |
| 18–64 | 5718 |
| 65+ | 3030 |
| Median household income | 41813 |
| Poverty rate | 24.07 |
| Homeownership rate | 68.02 |
| Unemployment rate | 13.02 |
| Median home value | 125900 |
| Gini index | 0.4976 |
| Vacancy rate | 21.46 |
| White | 4901 |
| Black | 5182 |
| Asian | 5 |
| Native | 10 |
| Hispanic/Latino | 436 |
| Bachelor's or higher | 1550 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 89% (congressional)
- [NC Senate District 2](/us/states/nc/districts/senate/2.md) — 89% (state senate)
- [NC House District 1](/us/states/nc/districts/house/1.md) — 89% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
