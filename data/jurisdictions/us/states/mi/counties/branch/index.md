---
type: Jurisdiction
title: "Branch County, MI"
classification: county
fips: "26023"
state: "MI"
demographics:
  population: 45300
  population_under_18: 10645
  population_18_64: 25868
  population_65_plus: 8787
  median_household_income: 63724
  poverty_rate: 16.43
  homeownership_rate: 77.67
  unemployment_rate: 5.66
  median_home_value: 162500
  gini_index: 0.421
  vacancy_rate: 19.38
  race_white: 39772
  race_black: 764
  race_asian: 228
  race_native: 175
  hispanic: 3071
  bachelors_plus: 6925
districts:
  - to: "us/states/mi/districts/05"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mi/districts/senate/17"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mi/districts/house/35"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Branch County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 45300 |
| Under 18 | 10645 |
| 18–64 | 25868 |
| 65+ | 8787 |
| Median household income | 63724 |
| Poverty rate | 16.43 |
| Homeownership rate | 77.67 |
| Unemployment rate | 5.66 |
| Median home value | 162500 |
| Gini index | 0.421 |
| Vacancy rate | 19.38 |
| White | 39772 |
| Black | 764 |
| Asian | 228 |
| Native | 175 |
| Hispanic/Latino | 3071 |
| Bachelor's or higher | 6925 |

## Districts

- [MI-05](/us/states/mi/districts/05.md) — 100% (congressional)
- [MI Senate District 17](/us/states/mi/districts/senate/17.md) — 100% (state senate)
- [MI House District 35](/us/states/mi/districts/house/35.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
