---
type: Jurisdiction
title: "Sanilac County, MI"
classification: county
fips: "26151"
state: "MI"
demographics:
  population: 40462
  population_under_18: 8472
  population_18_64: 22584
  population_65_plus: 9406
  median_household_income: 58863
  poverty_rate: 15.33
  homeownership_rate: 82.58
  unemployment_rate: 5.96
  median_home_value: 168300
  gini_index: 0.4323
  vacancy_rate: 19.49
  race_white: 37745
  race_black: 165
  race_asian: 115
  race_native: 48
  hispanic: 1732
  bachelors_plus: 6596
districts:
  - to: "us/states/mi/districts/09"
    rel: in-district
    area_weight: 0.6055
  - to: "us/states/mi/districts/senate/25"
    rel: in-district
    area_weight: 0.6059
  - to: "us/states/mi/districts/house/98"
    rel: in-district
    area_weight: 0.5816
  - to: "us/states/mi/districts/house/64"
    rel: in-district
    area_weight: 0.0243
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Sanilac County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 40462 |
| Under 18 | 8472 |
| 18–64 | 22584 |
| 65+ | 9406 |
| Median household income | 58863 |
| Poverty rate | 15.33 |
| Homeownership rate | 82.58 |
| Unemployment rate | 5.96 |
| Median home value | 168300 |
| Gini index | 0.4323 |
| Vacancy rate | 19.49 |
| White | 37745 |
| Black | 165 |
| Asian | 115 |
| Native | 48 |
| Hispanic/Latino | 1732 |
| Bachelor's or higher | 6596 |

## Districts

- [MI-09](/us/states/mi/districts/09.md) — 61% (congressional)
- [MI Senate District 25](/us/states/mi/districts/senate/25.md) — 61% (state senate)
- [MI House District 98](/us/states/mi/districts/house/98.md) — 58% (state house)
- [MI House District 64](/us/states/mi/districts/house/64.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
