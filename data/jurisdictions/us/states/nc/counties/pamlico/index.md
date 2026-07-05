---
type: Jurisdiction
title: "Pamlico County, NC"
classification: county
fips: "37137"
state: "NC"
demographics:
  population: 12390
  population_under_18: 1755
  population_18_64: 6849
  population_65_plus: 3786
  median_household_income: 59717
  poverty_rate: 15.15
  homeownership_rate: 82.88
  unemployment_rate: 5.11
  median_home_value: 216800
  gini_index: 0.4549
  vacancy_rate: 25.48
  race_white: 9116
  race_black: 2007
  race_asian: 73
  race_native: 23
  hispanic: 600
  bachelors_plus: 3705
districts:
  - to: "us/states/nc/districts/03"
    rel: in-district
    area_weight: 0.6888
  - to: "us/states/nc/districts/senate/2"
    rel: in-district
    area_weight: 0.6495
  - to: "us/states/nc/districts/house/79"
    rel: in-district
    area_weight: 0.6495
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Pamlico County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12390 |
| Under 18 | 1755 |
| 18–64 | 6849 |
| 65+ | 3786 |
| Median household income | 59717 |
| Poverty rate | 15.15 |
| Homeownership rate | 82.88 |
| Unemployment rate | 5.11 |
| Median home value | 216800 |
| Gini index | 0.4549 |
| Vacancy rate | 25.48 |
| White | 9116 |
| Black | 2007 |
| Asian | 73 |
| Native | 23 |
| Hispanic/Latino | 600 |
| Bachelor's or higher | 3705 |

## Districts

- [NC-03](/us/states/nc/districts/03.md) — 69% (congressional)
- [NC Senate District 2](/us/states/nc/districts/senate/2.md) — 65% (state senate)
- [NC House District 79](/us/states/nc/districts/house/79.md) — 65% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
