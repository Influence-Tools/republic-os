---
type: Jurisdiction
title: "Macon County, TN"
classification: county
fips: "47111"
state: "TN"
demographics:
  population: 26240
  population_under_18: 6583
  population_18_64: 15618
  population_65_plus: 4039
  median_household_income: 59177
  poverty_rate: 17.16
  homeownership_rate: 73.64
  unemployment_rate: 3.42
  median_home_value: 225700
  gini_index: 0.4384
  vacancy_rate: 14.33
  race_white: 23268
  race_black: 179
  race_asian: 46
  race_native: 9
  hispanic: 1837
  bachelors_plus: 2830
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/tn/districts/senate/12"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/tn/districts/house/38"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Macon County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26240 |
| Under 18 | 6583 |
| 18–64 | 15618 |
| 65+ | 4039 |
| Median household income | 59177 |
| Poverty rate | 17.16 |
| Homeownership rate | 73.64 |
| Unemployment rate | 3.42 |
| Median home value | 225700 |
| Gini index | 0.4384 |
| Vacancy rate | 14.33 |
| White | 23268 |
| Black | 179 |
| Asian | 46 |
| Native | 9 |
| Hispanic/Latino | 1837 |
| Bachelor's or higher | 2830 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 100% (congressional)
- [TN Senate District 12](/us/states/tn/districts/senate/12.md) — 100% (state senate)
- [TN House District 38](/us/states/tn/districts/house/38.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
