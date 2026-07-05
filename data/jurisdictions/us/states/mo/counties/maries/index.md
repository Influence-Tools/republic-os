---
type: Jurisdiction
title: "Maries County, MO"
classification: county
fips: "29125"
state: "MO"
demographics:
  population: 8450
  population_under_18: 1737
  population_18_64: 4851
  population_65_plus: 1862
  median_household_income: 59455
  poverty_rate: 13.51
  homeownership_rate: 78.33
  unemployment_rate: 4.79
  median_home_value: 219100
  gini_index: 0.4185
  vacancy_rate: 19.55
  race_white: 7830
  race_black: 18
  race_asian: 0
  race_native: 103
  hispanic: 175
  bachelors_plus: 1535
districts:
  - to: "us/states/mo/districts/03"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/mo/districts/senate/16"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/143"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Maries County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8450 |
| Under 18 | 1737 |
| 18–64 | 4851 |
| 65+ | 1862 |
| Median household income | 59455 |
| Poverty rate | 13.51 |
| Homeownership rate | 78.33 |
| Unemployment rate | 4.79 |
| Median home value | 219100 |
| Gini index | 0.4185 |
| Vacancy rate | 19.55 |
| White | 7830 |
| Black | 18 |
| Asian | 0 |
| Native | 103 |
| Hispanic/Latino | 175 |
| Bachelor's or higher | 1535 |

## Districts

- [MO-03](/us/states/mo/districts/03.md) — 100% (congressional)
- [MO Senate District 16](/us/states/mo/districts/senate/16.md) — 100% (state senate)
- [MO House District 143](/us/states/mo/districts/house/143.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
