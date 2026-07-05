---
type: Jurisdiction
title: "Windsor County, VT"
classification: county
fips: "50027"
state: "VT"
demographics:
  population: 57990
  population_under_18: 10186
  population_18_64: 33009
  population_65_plus: 14795
  median_household_income: 77594
  poverty_rate: 9.22
  homeownership_rate: 74.84
  unemployment_rate: 4.37
  median_home_value: 296400
  gini_index: 0.4667
  vacancy_rate: 27.41
  race_white: 53730
  race_black: 291
  race_asian: 596
  race_native: 44
  hispanic: 1327
  bachelors_plus: 26971
districts:
  - to: "us/states/vt/districts/00"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, vt]
timestamp: "2026-07-03"
---

# Windsor County, VT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 57990 |
| Under 18 | 10186 |
| 18–64 | 33009 |
| 65+ | 14795 |
| Median household income | 77594 |
| Poverty rate | 9.22 |
| Homeownership rate | 74.84 |
| Unemployment rate | 4.37 |
| Median home value | 296400 |
| Gini index | 0.4667 |
| Vacancy rate | 27.41 |
| White | 53730 |
| Black | 291 |
| Asian | 596 |
| Native | 44 |
| Hispanic/Latino | 1327 |
| Bachelor's or higher | 26971 |

## Districts

- [VT-00](/us/states/vt/districts/00.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
