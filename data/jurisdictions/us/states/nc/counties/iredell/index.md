---
type: Jurisdiction
title: "Iredell County, NC"
classification: county
fips: "37097"
state: "NC"
demographics:
  population: 196544
  population_under_18: 43749
  population_18_64: 119856
  population_65_plus: 32939
  median_household_income: 81419
  poverty_rate: 10.03
  homeownership_rate: 71.85
  unemployment_rate: 4.16
  median_home_value: 321400
  gini_index: 0.4722
  vacancy_rate: 9.33
  race_white: 145582
  race_black: 22101
  race_asian: 4801
  race_native: 351
  hispanic: 18191
  bachelors_plus: 62122
districts:
  - to: "us/states/nc/districts/10"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/nc/districts/senate/37"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nc/districts/house/84"
    rel: in-district
    area_weight: 0.7397
  - to: "us/states/nc/districts/house/95"
    rel: in-district
    area_weight: 0.1659
  - to: "us/states/nc/districts/house/89"
    rel: in-district
    area_weight: 0.0943
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Iredell County, NC

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 196544 |
| Under 18 | 43749 |
| 18–64 | 119856 |
| 65+ | 32939 |
| Median household income | 81419 |
| Poverty rate | 10.03 |
| Homeownership rate | 71.85 |
| Unemployment rate | 4.16 |
| Median home value | 321400 |
| Gini index | 0.4722 |
| Vacancy rate | 9.33 |
| White | 145582 |
| Black | 22101 |
| Asian | 4801 |
| Native | 351 |
| Hispanic/Latino | 18191 |
| Bachelor's or higher | 62122 |

## Districts

- [NC-10](/us/states/nc/districts/10.md) — 100% (congressional)
- [NC Senate District 37](/us/states/nc/districts/senate/37.md) — 100% (state senate)
- [NC House District 84](/us/states/nc/districts/house/84.md) — 74% (state house)
- [NC House District 95](/us/states/nc/districts/house/95.md) — 17% (state house)
- [NC House District 89](/us/states/nc/districts/house/89.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
