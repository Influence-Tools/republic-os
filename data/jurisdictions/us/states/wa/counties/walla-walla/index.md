---
type: Jurisdiction
title: "Walla Walla County, WA"
classification: county
fips: "53071"
state: "WA"
demographics:
  population: 62161
  population_under_18: 12787
  population_18_64: 36965
  population_65_plus: 12409
  median_household_income: 74202
  poverty_rate: 12.06
  homeownership_rate: 64.98
  unemployment_rate: 6.23
  median_home_value: 408900
  gini_index: 0.4618
  vacancy_rate: 7.77
  race_white: 45047
  race_black: 1032
  race_asian: 1151
  race_native: 756
  hispanic: 14816
  bachelors_plus: 17835
districts:
  - to: "us/states/wa/districts/05"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wa/districts/senate/16"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wa/districts/house/16"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Walla Walla County, WA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 62161 |
| Under 18 | 12787 |
| 18–64 | 36965 |
| 65+ | 12409 |
| Median household income | 74202 |
| Poverty rate | 12.06 |
| Homeownership rate | 64.98 |
| Unemployment rate | 6.23 |
| Median home value | 408900 |
| Gini index | 0.4618 |
| Vacancy rate | 7.77 |
| White | 45047 |
| Black | 1032 |
| Asian | 1151 |
| Native | 756 |
| Hispanic/Latino | 14816 |
| Bachelor's or higher | 17835 |

## Districts

- [WA-05](/us/states/wa/districts/05.md) — 100% (congressional)
- [WA Senate District 16](/us/states/wa/districts/senate/16.md) — 100% (state senate)
- [WA House District 16](/us/states/wa/districts/house/16.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
