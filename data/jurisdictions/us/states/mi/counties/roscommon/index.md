---
type: Jurisdiction
title: "Roscommon County, MI"
classification: county
fips: "26143"
state: "MI"
demographics:
  population: 23737
  population_under_18: 3396
  population_18_64: 12149
  population_65_plus: 8192
  median_household_income: 55246
  poverty_rate: 15.54
  homeownership_rate: 85.44
  unemployment_rate: 4.74
  median_home_value: 158700
  gini_index: 0.4681
  vacancy_rate: 50.12
  race_white: 22108
  race_black: 160
  race_asian: 28
  race_native: 49
  hispanic: 483
  bachelors_plus: 5430
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/senate/36"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/house/105"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Roscommon County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23737 |
| Under 18 | 3396 |
| 18–64 | 12149 |
| 65+ | 8192 |
| Median household income | 55246 |
| Poverty rate | 15.54 |
| Homeownership rate | 85.44 |
| Unemployment rate | 4.74 |
| Median home value | 158700 |
| Gini index | 0.4681 |
| Vacancy rate | 50.12 |
| White | 22108 |
| Black | 160 |
| Asian | 28 |
| Native | 49 |
| Hispanic/Latino | 483 |
| Bachelor's or higher | 5430 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 100% (congressional)
- [MI Senate District 36](/us/states/mi/districts/senate/36.md) — 100% (state senate)
- [MI House District 105](/us/states/mi/districts/house/105.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
