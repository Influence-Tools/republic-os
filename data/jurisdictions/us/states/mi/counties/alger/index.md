---
type: Jurisdiction
title: "Alger County, MI"
classification: county
fips: "26003"
state: "MI"
demographics:
  population: 8762
  population_under_18: 1284
  population_18_64: 5098
  population_65_plus: 2380
  median_household_income: 61286
  poverty_rate: 10.36
  homeownership_rate: 86.29
  unemployment_rate: 6.8
  median_home_value: 176200
  gini_index: 0.4042
  vacancy_rate: 43.2
  race_white: 7178
  race_black: 670
  race_asian: 23
  race_native: 202
  hispanic: 154
  bachelors_plus: 1852
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.1856
  - to: "us/states/mi/districts/senate/38"
    rel: in-district
    area_weight: 0.1839
  - to: "us/states/mi/districts/house/109"
    rel: in-district
    area_weight: 0.1838
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Alger County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8762 |
| Under 18 | 1284 |
| 18–64 | 5098 |
| 65+ | 2380 |
| Median household income | 61286 |
| Poverty rate | 10.36 |
| Homeownership rate | 86.29 |
| Unemployment rate | 6.8 |
| Median home value | 176200 |
| Gini index | 0.4042 |
| Vacancy rate | 43.2 |
| White | 7178 |
| Black | 670 |
| Asian | 23 |
| Native | 202 |
| Hispanic/Latino | 154 |
| Bachelor's or higher | 1852 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 19% (congressional)
- [MI Senate District 38](/us/states/mi/districts/senate/38.md) — 18% (state senate)
- [MI House District 109](/us/states/mi/districts/house/109.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
