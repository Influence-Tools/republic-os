---
type: Jurisdiction
title: "Baltimore city, MD"
classification: county
fips: "24510"
state: "MD"
demographics:
  population: 573243
  population_under_18: 119618
  population_18_64: 366023
  population_65_plus: 87602
  median_household_income: 62177
  poverty_rate: 19.75
  homeownership_rate: 47.51
  unemployment_rate: 6.54
  median_home_value: 229600
  gini_index: 0.508
  vacancy_rate: 13.34
  race_white: 154160
  race_black: 339623
  race_asian: 14895
  race_native: 2411
  hispanic: 47018
  bachelors_plus: 217729
districts:
  - to: "us/states/md/districts/07"
    rel: in-district
    area_weight: 0.8716
  - to: "us/states/md/districts/02"
    rel: in-district
    area_weight: 0.0663
  - to: "us/states/md/districts/senate/46"
    rel: in-district
    area_weight: 0.2872
  - to: "us/states/md/districts/senate/41"
    rel: in-district
    area_weight: 0.2262
  - to: "us/states/md/districts/senate/45"
    rel: in-district
    area_weight: 0.1765
  - to: "us/states/md/districts/senate/40"
    rel: in-district
    area_weight: 0.1558
  - to: "us/states/md/districts/senate/43"
    rel: in-district
    area_weight: 0.0928
  - to: "us/states/md/districts/house/46"
    rel: in-district
    area_weight: 0.2872
  - to: "us/states/md/districts/house/41"
    rel: in-district
    area_weight: 0.2262
  - to: "us/states/md/districts/house/45"
    rel: in-district
    area_weight: 0.1765
  - to: "us/states/md/districts/house/40"
    rel: in-district
    area_weight: 0.1558
  - to: "us/states/md/districts/house/43a"
    rel: in-district
    area_weight: 0.0928
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Baltimore city, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 573243 |
| Under 18 | 119618 |
| 18–64 | 366023 |
| 65+ | 87602 |
| Median household income | 62177 |
| Poverty rate | 19.75 |
| Homeownership rate | 47.51 |
| Unemployment rate | 6.54 |
| Median home value | 229600 |
| Gini index | 0.508 |
| Vacancy rate | 13.34 |
| White | 154160 |
| Black | 339623 |
| Asian | 14895 |
| Native | 2411 |
| Hispanic/Latino | 47018 |
| Bachelor's or higher | 217729 |

## Districts

- [MD-07](/us/states/md/districts/07.md) — 87% (congressional)
- [MD-02](/us/states/md/districts/02.md) — 7% (congressional)
- [MD Senate District 46](/us/states/md/districts/senate/46.md) — 29% (state senate)
- [MD Senate District 41](/us/states/md/districts/senate/41.md) — 23% (state senate)
- [MD Senate District 45](/us/states/md/districts/senate/45.md) — 18% (state senate)
- [MD Senate District 40](/us/states/md/districts/senate/40.md) — 16% (state senate)
- [MD Senate District 43](/us/states/md/districts/senate/43.md) — 9% (state senate)
- [MD House District 46](/us/states/md/districts/house/46.md) — 29% (state house)
- [MD House District 41](/us/states/md/districts/house/41.md) — 23% (state house)
- [MD House District 45](/us/states/md/districts/house/45.md) — 18% (state house)
- [MD House District 40](/us/states/md/districts/house/40.md) — 16% (state house)
- [MD House District 43A](/us/states/md/districts/house/43a.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
