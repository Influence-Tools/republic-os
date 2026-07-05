---
type: Jurisdiction
title: "Pacific County, WA"
classification: county
fips: "53049"
state: "WA"
demographics:
  population: 23994
  population_under_18: 3602
  population_18_64: 12471
  population_65_plus: 7921
  median_household_income: 67081
  poverty_rate: 10.35
  homeownership_rate: 81.81
  unemployment_rate: 5.15
  median_home_value: 334800
  gini_index: 0.4882
  vacancy_rate: 32.76
  race_white: 19714
  race_black: 157
  race_asian: 374
  race_native: 467
  hispanic: 2378
  bachelors_plus: 6266
districts:
  - to: "us/states/wa/districts/03"
    rel: in-district
    area_weight: 0.7697
  - to: "us/states/wa/districts/senate/19"
    rel: in-district
    area_weight: 0.7692
  - to: "us/states/wa/districts/house/19"
    rel: in-district
    area_weight: 0.7692
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Pacific County, WA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23994 |
| Under 18 | 3602 |
| 18–64 | 12471 |
| 65+ | 7921 |
| Median household income | 67081 |
| Poverty rate | 10.35 |
| Homeownership rate | 81.81 |
| Unemployment rate | 5.15 |
| Median home value | 334800 |
| Gini index | 0.4882 |
| Vacancy rate | 32.76 |
| White | 19714 |
| Black | 157 |
| Asian | 374 |
| Native | 467 |
| Hispanic/Latino | 2378 |
| Bachelor's or higher | 6266 |

## Districts

- [WA-03](/us/states/wa/districts/03.md) — 77% (congressional)
- [WA Senate District 19](/us/states/wa/districts/senate/19.md) — 77% (state senate)
- [WA House District 19](/us/states/wa/districts/house/19.md) — 77% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
