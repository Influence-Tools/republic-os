---
type: Jurisdiction
title: "Sheridan County, MT"
classification: county
fips: "30091"
state: "MT"
demographics:
  population: 3669
  population_under_18: 802
  population_18_64: 2034
  population_65_plus: 833
  median_household_income: 70147
  poverty_rate: 10.42
  homeownership_rate: 71.82
  unemployment_rate: 2.06
  median_home_value: 124000
  gini_index: 0.4759
  vacancy_rate: 27.68
  race_white: 3321
  race_black: 0
  race_asian: 24
  race_native: 71
  hispanic: 145
  bachelors_plus: 861
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/mt/districts/senate/15"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mt/districts/house/29"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Sheridan County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3669 |
| Under 18 | 802 |
| 18–64 | 2034 |
| 65+ | 833 |
| Median household income | 70147 |
| Poverty rate | 10.42 |
| Homeownership rate | 71.82 |
| Unemployment rate | 2.06 |
| Median home value | 124000 |
| Gini index | 0.4759 |
| Vacancy rate | 27.68 |
| White | 3321 |
| Black | 0 |
| Asian | 24 |
| Native | 71 |
| Hispanic/Latino | 145 |
| Bachelor's or higher | 861 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 15](/us/states/mt/districts/senate/15.md) — 100% (state senate)
- [MT House District 29](/us/states/mt/districts/house/29.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
