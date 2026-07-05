---
type: Jurisdiction
title: "Clallam County, WA"
classification: county
fips: "53009"
state: "WA"
demographics:
  population: 77813
  population_under_18: 12527
  population_18_64: 40219
  population_65_plus: 25067
  median_household_income: 70370
  poverty_rate: 10.58
  homeownership_rate: 73.72
  unemployment_rate: 5.09
  median_home_value: 421800
  gini_index: 0.4505
  vacancy_rate: 9.24
  race_white: 63706
  race_black: 656
  race_asian: 1384
  race_native: 2743
  hispanic: 5273
  bachelors_plus: 26850
districts:
  - to: "us/states/wa/districts/06"
    rel: in-district
    area_weight: 0.663
  - to: "us/states/wa/districts/senate/24"
    rel: in-district
    area_weight: 0.6616
  - to: "us/states/wa/districts/house/24"
    rel: in-district
    area_weight: 0.6616
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Clallam County, WA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 77813 |
| Under 18 | 12527 |
| 18–64 | 40219 |
| 65+ | 25067 |
| Median household income | 70370 |
| Poverty rate | 10.58 |
| Homeownership rate | 73.72 |
| Unemployment rate | 5.09 |
| Median home value | 421800 |
| Gini index | 0.4505 |
| Vacancy rate | 9.24 |
| White | 63706 |
| Black | 656 |
| Asian | 1384 |
| Native | 2743 |
| Hispanic/Latino | 5273 |
| Bachelor's or higher | 26850 |

## Districts

- [WA-06](/us/states/wa/districts/06.md) — 66% (congressional)
- [WA Senate District 24](/us/states/wa/districts/senate/24.md) — 66% (state senate)
- [WA House District 24](/us/states/wa/districts/house/24.md) — 66% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
