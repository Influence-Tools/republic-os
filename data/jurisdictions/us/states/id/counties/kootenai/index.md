---
type: Jurisdiction
title: "Kootenai County, ID"
classification: county
fips: "16055"
state: "ID"
demographics:
  population: 181996
  population_under_18: 40656
  population_18_64: 104749
  population_65_plus: 36591
  median_household_income: 81861
  poverty_rate: 9.04
  homeownership_rate: 71.28
  unemployment_rate: 3.27
  median_home_value: 518700
  gini_index: 0.4304
  vacancy_rate: 11.32
  race_white: 158537
  race_black: 644
  race_asian: 1264
  race_native: 1493
  hispanic: 10298
  bachelors_plus: 50872
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/id/districts/senate/2"
    rel: in-district
    area_weight: 0.5815
  - to: "us/states/id/districts/senate/5"
    rel: in-district
    area_weight: 0.2131
  - to: "us/states/id/districts/senate/3"
    rel: in-district
    area_weight: 0.1904
  - to: "us/states/id/districts/senate/4"
    rel: in-district
    area_weight: 0.0149
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Kootenai County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 181996 |
| Under 18 | 40656 |
| 18–64 | 104749 |
| 65+ | 36591 |
| Median household income | 81861 |
| Poverty rate | 9.04 |
| Homeownership rate | 71.28 |
| Unemployment rate | 3.27 |
| Median home value | 518700 |
| Gini index | 0.4304 |
| Vacancy rate | 11.32 |
| White | 158537 |
| Black | 644 |
| Asian | 1264 |
| Native | 1493 |
| Hispanic/Latino | 10298 |
| Bachelor's or higher | 50872 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 100% (congressional)
- [ID Senate District 2](/us/states/id/districts/senate/2.md) — 58% (state senate)
- [ID Senate District 5](/us/states/id/districts/senate/5.md) — 21% (state senate)
- [ID Senate District 3](/us/states/id/districts/senate/3.md) — 19% (state senate)
- [ID Senate District 4](/us/states/id/districts/senate/4.md) — 1% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
