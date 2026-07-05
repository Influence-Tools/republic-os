---
type: Jurisdiction
title: "Northwest Arctic Borough, AK"
classification: county
fips: "02188"
state: "AK"
demographics:
  population: 7441
  population_under_18: 2984
  population_18_64: 2383
  population_65_plus: 2074
  median_household_income: 84018
  poverty_rate: 17.86
  homeownership_rate: 64.38
  unemployment_rate: 16.66
  median_home_value: 199100
  gini_index: 0.4251
  vacancy_rate: 33.49
  race_white: 726
  race_black: 42
  race_asian: 116
  race_native: 5997
  hispanic: 173
  bachelors_plus: 593
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.9075
  - to: "us/states/ak/districts/senate/t"
    rel: in-district
    area_weight: 0.8957
  - to: "us/states/ak/districts/house/40"
    rel: in-district
    area_weight: 0.8957
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Northwest Arctic Borough, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7441 |
| Under 18 | 2984 |
| 18–64 | 2383 |
| 65+ | 2074 |
| Median household income | 84018 |
| Poverty rate | 17.86 |
| Homeownership rate | 64.38 |
| Unemployment rate | 16.66 |
| Median home value | 199100 |
| Gini index | 0.4251 |
| Vacancy rate | 33.49 |
| White | 726 |
| Black | 42 |
| Asian | 116 |
| Native | 5997 |
| Hispanic/Latino | 173 |
| Bachelor's or higher | 593 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 91% (congressional)
- [AK Senate District T](/us/states/ak/districts/senate/t.md) — 90% (state senate)
- [AK House District 40](/us/states/ak/districts/house/40.md) — 90% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
