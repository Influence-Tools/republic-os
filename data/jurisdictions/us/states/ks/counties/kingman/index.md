---
type: Jurisdiction
title: "Kingman County, KS"
classification: county
fips: "20095"
state: "KS"
demographics:
  population: 7186
  population_under_18: 1641
  population_18_64: 4129
  population_65_plus: 1416
  median_household_income: 59842
  poverty_rate: 10.33
  homeownership_rate: 66.27
  unemployment_rate: 2.22
  median_home_value: 111100
  gini_index: 0.4202
  vacancy_rate: 14.08
  race_white: 6675
  race_black: 18
  race_asian: 3
  race_native: 27
  hispanic: 294
  bachelors_plus: 1644
districts:
  - to: "us/states/ks/districts/04"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/senate/34"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/114"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Kingman County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7186 |
| Under 18 | 1641 |
| 18–64 | 4129 |
| 65+ | 1416 |
| Median household income | 59842 |
| Poverty rate | 10.33 |
| Homeownership rate | 66.27 |
| Unemployment rate | 2.22 |
| Median home value | 111100 |
| Gini index | 0.4202 |
| Vacancy rate | 14.08 |
| White | 6675 |
| Black | 18 |
| Asian | 3 |
| Native | 27 |
| Hispanic/Latino | 294 |
| Bachelor's or higher | 1644 |

## Districts

- [KS-04](/us/states/ks/districts/04.md) — 100% (congressional)
- [KS Senate District 34](/us/states/ks/districts/senate/34.md) — 100% (state senate)
- [KS House District 114](/us/states/ks/districts/house/114.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
