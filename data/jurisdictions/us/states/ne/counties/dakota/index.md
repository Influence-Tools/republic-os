---
type: Jurisdiction
title: "Dakota County, NE"
classification: county
fips: "31043"
state: "NE"
demographics:
  population: 21354
  population_under_18: 6297
  population_18_64: 12315
  population_65_plus: 2742
  median_household_income: 70329
  poverty_rate: 11.54
  homeownership_rate: 63.91
  unemployment_rate: 4.81
  median_home_value: 185700
  gini_index: 0.4212
  vacancy_rate: 4.47
  race_white: 9548
  race_black: 1852
  race_asian: 646
  race_native: 722
  hispanic: 8878
  bachelors_plus: 2313
districts:
  - to: "us/states/ne/districts/03"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Dakota County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21354 |
| Under 18 | 6297 |
| 18–64 | 12315 |
| 65+ | 2742 |
| Median household income | 70329 |
| Poverty rate | 11.54 |
| Homeownership rate | 63.91 |
| Unemployment rate | 4.81 |
| Median home value | 185700 |
| Gini index | 0.4212 |
| Vacancy rate | 4.47 |
| White | 9548 |
| Black | 1852 |
| Asian | 646 |
| Native | 722 |
| Hispanic/Latino | 8878 |
| Bachelor's or higher | 2313 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
