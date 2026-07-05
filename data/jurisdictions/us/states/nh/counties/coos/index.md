---
type: Jurisdiction
title: "Coos County, NH"
classification: county
fips: "33007"
state: "NH"
demographics:
  population: 31271
  population_under_18: 5014
  population_18_64: 18105
  population_65_plus: 8152
  median_household_income: 57677
  poverty_rate: 13.21
  homeownership_rate: 74.25
  unemployment_rate: 4.28
  median_home_value: 188900
  gini_index: 0.4884
  vacancy_rate: 32.15
  race_white: 29158
  race_black: 690
  race_asian: 45
  race_native: 64
  hispanic: 741
  bachelors_plus: 6586
districts:
  - to: "us/states/nh/districts/02"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/nh/districts/senate/1"
    rel: in-district
    area_weight: 0.9128
  - to: "us/states/nh/districts/senate/3"
    rel: in-district
    area_weight: 0.0865
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nh]
timestamp: "2026-07-03"
---

# Coos County, NH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31271 |
| Under 18 | 5014 |
| 18–64 | 18105 |
| 65+ | 8152 |
| Median household income | 57677 |
| Poverty rate | 13.21 |
| Homeownership rate | 74.25 |
| Unemployment rate | 4.28 |
| Median home value | 188900 |
| Gini index | 0.4884 |
| Vacancy rate | 32.15 |
| White | 29158 |
| Black | 690 |
| Asian | 45 |
| Native | 64 |
| Hispanic/Latino | 741 |
| Bachelor's or higher | 6586 |

## Districts

- [NH-02](/us/states/nh/districts/02.md) — 100% (congressional)
- [NH Senate District 1](/us/states/nh/districts/senate/1.md) — 91% (state senate)
- [NH Senate District 3](/us/states/nh/districts/senate/3.md) — 9% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
